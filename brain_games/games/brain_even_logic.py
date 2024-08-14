import random


rules = 'Answer "yes" if the number is even, otherwise answer "no".'


def get_question_and_correct_answer(start=0, end=1000):
    question = random.randint(start, end)
    correct_answer = 'yes' if question % 2 == 0 else 'no'
    return question, correct_answer
