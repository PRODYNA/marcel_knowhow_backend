import json

from jni_openai import OpenAi


REL_FILE_PAHT = "db/questions_input/question_ai_output.json"
NO_QUESTIONS = 50


class Item:
	def __init__(self, id: int, question: str, yes_answer: bool):
		self.id = id
		self.question = question
		self.yes_answer = yes_answer


def write_questions_to_json_file() -> None:
	open_ai = OpenAi()
	ai_questions = open_ai.create_quizz_questions(NO_QUESTIONS)

	with open(REL_FILE_PAHT, "w") as file:
		file.write(ai_questions)


def read_questions_from_json_file() -> None:
	with open(REL_FILE_PAHT, "r") as file:
		ai_questions = file.read()
		questions: list[dict] = json.loads(ai_questions)
		for question in questions:
			item = Item(question["id"], question["question"], question["yes_answer"])
			print(f'Item: "{item}"')


def main() -> None:
	write_questions_to_json_file()
	read_questions_from_json_file()


if __name__ == "__main__":
	main()
