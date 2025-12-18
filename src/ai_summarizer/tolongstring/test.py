# from pdf_to_string import pdf_bytes_to_text_string
# import streamlit as st

# uploaded = st.file_uploader("Upload PDF", type=["pdf"])
# if uploaded:
#     text = pdf_bytes_to_text_string(uploaded.read())

import sys
import io
from ai_summarizer.tolongstring.pdf_to_string import pdf_bytes_to_text_string
from ai_summarizer.quiz.generator import QuizGenerator


if len(sys.argv) != 2:
	print("Usage: python test_pdf_extract.py <file.pdf>")
	sys.exit(1)

pdf_path = sys.argv[1]

with open(pdf_path, "rb") as f:
	pdf_bytes = f.read()

text = pdf_bytes_to_text_string(pdf_bytes)

print("----- EXTRACTED TEXT -----\n")
print(text)  # preview first chars
print("\n----- END  -----")


print("----------------------------------------------------------------")
print("||                           TEST                            ||")
print("----------------------------------------------------------------")
gen = QuizGenerator()
quiz = gen.generate(text)
print("Total number of questions: " + str(quiz.total_questions) + "\n")
print("Total number of words in the text: " + str(len(text.strip())) + "\n")
for q in quiz.questions:
	print(f"------------------------- QUESTION {quiz.questions.index(q) + 1} ---------------------------\n")
	print("DIFFICULTY: " + q.difficulty + "\n")
	print("QUESTION : " + q.question + "\n")
	print("OPTIONS:")
	for opt in q.options:
		print(str(q.options.index(opt) + 1) + ". " + opt)
	print()
	print("ANSWER : " + q.answer + "\n")
print("--------------------------------------------------------------------")
print("||                           END TEST                             ||")
print("--------------------------------------------------------------------\n\n\n")

