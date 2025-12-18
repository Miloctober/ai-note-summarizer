
from .models import QuizOutput, QuizQuestion, MODEL_NAME


import random
import ollama
import json
import math

WORDS_PER_CHUNK = 1000      # number of words per chunk of text
OVERLAP = 100               # number of words that will overlap in each chunk

class QuizGenerator:

	def __init__(self, model_name = MODEL_NAME, max_questions = 30):
		self.model_name = model_name
		self.max_questions = max_questions


	def normalize_options(self, answer, options):
		'''
		Normalize and deduplicate a list of options for multiple choices questions
		
		:param self: Instance reference
		:param answer (str): The correct answer of the multiple-choice question
		:param options (list): A list of all options of the multiple-choice question 

		returns: a list of cleaned, normalized and deduplicated options or 0 if there is less than 4 options
		'''
		cleaned_options = []										# list of cleaned, normalized options

		for opt in options:
			if isinstance(opt, str):								# check if the option is a string
				tmp = opt.strip()									# remove all whitespaces at the beginning and at the end of the string
				if (tmp and (tmp not in cleaned_options)):			# check if there is already an instance of the object in the final list
					cleaned_options.append(tmp)						# add the object to the list

		if (answer not in cleaned_options):							# check if the right answer is in the list
			cleaned_options.insert(0, answer)						# if not, insert it at the beginning of the list
		
		if (len(cleaned_options) < 4):								# if there is less than 4 options, return 0
			print("Less than 4 answers, stop.")
			return (0)

		while (len(cleaned_options) > 4):							# if there is more than 4 options, remove the ones at the end until there is 4
			cleaned_options.pop()
		
		random.shuffle(cleaned_options)								# shuffle the list so that the answer is not always at the beginning
		return (cleaned_options)
		


	def chunk_text(self, text, max_words = WORDS_PER_CHUNK, overlap = OVERLAP):
		'''
		Seperate a text into smaller chunks of text, including a small overlap to make sure it is coherent
		
		:param self: Instance reference
		:param text (str): The text which will be separated
		:param max_words (int): The maximum number of words the chunk will have
		:param overlap (int): The number of words which will overlap in each chunk

		yields: A chunk of text containing up to 'max_words' words 
		'''
		words = list(text.split())								# make a list conataining all the wrods of the text
		step = max_words - overlap								# count the step of each iteration
		if (step < 0):											# check if the step is negative to avoid an infinite loop
			return
		for i in range(0, len(words), step):					# loop through the text with 'step' steps
			yield " ".join(words[i:i + max_words])				# returns the next chunk at each call if the function

		

	def generate(self, text) -> QuizOutput:
		'''
		Generate a multiple-choice quiz with an external LLM (Ollana, model llama3:8b when writing this function)
		
		:param self: Instance reference
		:param text: The source text which the questions will be extracted from

		:return: an object which contains the generated questions, the total number of questions and the source text
		:rtype: QuizOutput

		Notes: 
			- The number of questions is dynamically determined based on the length of the text (for a maximum of 'self.max_questions' questions)
			- Questions are generated in chunks to not go over the limit of Tokens
			- Each questions has exactly 4 options to choose from, including the right answer
			- If a question or its options are invalid, it is discarded
			- For each question, keep in memory some keywords to make sure to not have duplicates questions
		'''
		if (not isinstance(text, str)):								# check if text is a string, is empty or is too short
			raise TypeError("Text given is not of string type.")
		if ((not text) or (not text.strip())):
			raise ValueError("Text given is empty.")
		
		text = text.strip()
		if (len(text) < 100):
			raise ValueError("Text given is too short.")
		
		nb_words = len(text.split())												# count the number of words in the text
		nb_questions = max(1, min(self.max_questions, nb_words // 100 or 1))		# calculate the number of questions based on the number of words (1 question for 100 words)

		per_chunk_questions = max(1, math.ceil(nb_questions / (nb_words / (WORDS_PER_CHUNK - OVERLAP))))	# calculate the number of questions we need per chunk
		remaining = nb_questions																			# keep track of the remaining number of question we have

		questions = []			# list which will contain all questions
		summary = []			# list containing a summary of keywords for each questions

		for chunk in self.chunk_text(text):			# go through the source text per chunks
			if (remaining == 0):					# break the loop if the number of remaining question is 0
				break

			q_to_request = min(per_chunk_questions, remaining)		# check the number of question for this chunk

			system_prompt = (
				"You are an expert educator. You create concise, factual multiple-choice questions from the provided material."
			)																														# System prompt sets the overall behavior of the LLM

			user_prompt = (
				f"Source material:\n{chunk}\n\n"
				f"Return up to {q_to_request} multiple-choice questions as JSON with this schema:\n"
				'{ "questions": [ { "question": str, "answer": str, "options": [str, str, str, str], '
				'"difficulty": "easy" | "medium" | "hard", "keywords": [str, str, str] } ] }\n'
				"Use only facts from the source. keep questions clear and non-overlapping. "
				"Always provide at least 4 options including the correct answer."
				f"Avoid overlapping with these already asked topics: {summary}."
				"Don't put the answer of the question in the question"
				)																													# User Prompt is the specific task the LLM has to do

			try:
				response = ollama.chat(
					model = self.model_name,									# specify which model to use
					format = "json",											# return a JSON
					messages =[
						{"role" : "system", "content" : system_prompt},			# system message defining overall behavior
						{"role" : "user", "content" : user_prompt}				# user message containing the task and the data
					]
				)
			except Exception:
				raise RuntimeError("Ollama generation failed")
			
			try:
				payload = json.loads(response["message"]["content"])					# parse the response of the LLM in JSON
			except Exception:
				raise RuntimeError("Failed to parse Ollama response as JSON")
			
			for q in payload.get("questions", []):										# go through the generated questions
				q_text = str(q.get("question") or " ").strip()							# extract and parse the question
				answer = str(q.get("answer") or " ").strip()							# extract and parse the answer
				difficulty = str(q.get("difficulty") or "medium").strip().lower()		# extract and parse the difficulty, set it to 'medium' if there is an error
				if (difficulty not in ["easy", "medium", "hard"]):
					difficulty = "medium"

				if (not q_text or not answer):											# check if the question or the answer is empty, if it is, go to the next question
					continue
				options = self.normalize_options(answer, q.get("options", []))			# extract and parse all the options with the 'normalize_option()' function
				if (options == 0):														# if there is an error during the parsing, go to the next question
					continue
				else :																	# append the Object with all data to the list
					questions.append(
						QuizQuestion(
							question = q_text,
							answer = answer,
							options = options,
							difficulty = difficulty
						)
					)
					remaining -= 1														# substract 1 to the remaining questions we have to add

					keywords = q.get("keywords") or []									# extracts the keywords of the question
					norm_keywords = []													# the list of normalized keywords
					for k in keywords:													# go throught the keywords, normalize them and add them to the list
						if isinstance(k, str):
							t = k.strip().lower()
							if t:
								norm_keywords.append(t)
					summary = "; ".join(norm_keywords[:3])								# add the keywords to the summary the LLM will read

			if (not questions):
				raise RuntimeError("No valid questions were generated")
		
		questions = questions[:nb_questions]											# remove the excess questions
		
		return (QuizOutput(
			questions = questions,
			total_questions = len(questions),
			source_text = text
		))																				# returns the questions, the total number of question and the source text
																						# as an 'QuizOutput' object

