from generator import QuizGenerator
from test_text import test_text
from src.quiz.models import QuizOutput, QuizQuestion, MODEL_NAME

for i in range (1, len(test_text) + 1):
	print(f"----------------------------------------------------------------")
	print(f"||                           TEST {i}                           ||")
	print(f"----------------------------------------------------------------")
	text = test_text[i - 1]
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
	print(f"--------------------------------------------------------------------")
	print(f"||                           END TEST {i}                           ||")
	print(f"--------------------------------------------------------------------\n\n\n")

