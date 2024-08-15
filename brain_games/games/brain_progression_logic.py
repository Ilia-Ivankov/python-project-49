import random


rules = 'What number is missing in the progression?'


def get_question_and_answer(start=0, end=50):
    number_of_progression = random.randint(1, end)
    progression = []
    first_number_of_progression = random.randint(start, end)
    length_of_progression = random.randint(5, 10)
    for _ in range(length_of_progression):
        progression.append(str(first_number_of_progression))
        first_number_of_progression += number_of_progression
    random_number = random.randint(0, length_of_progression - 1)
    correct_answer = progression[random_number]
    correct_answer = str(correct_answer)
    progression[random_number] = ".."
    question = ' '.join(progression)
    return question, correct_answer
