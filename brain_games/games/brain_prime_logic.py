import random


rules = 'Answer "yes" if given number is prime, otherwise answer "no".'


def is_prime(number):
    k = 2
    while k != number:
        if number % k == 0:
            return False
        else:
            k += 1
    return k == number


def get_question_and_correct_answer(start=0, end=100):
    question = random.randint(start, end)
    correct_answer = 'yes' if is_prime(question) else 'no'
    return question, correct_answer
