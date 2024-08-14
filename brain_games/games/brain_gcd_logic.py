import random


rules = 'Find the greatest common divisor of given numbers.'


def find_gcd(number1, number2):
    while number1 != number2:
        if number1 > number2:
            number1 -= number2
        if number2 > number1:
            number2 -= number1
    return number1


def get_question_and_correct_answer(start=0, end=100):
    number1 = random.randint(start, end)
    number2 = random.randint(start, end)
    question = str(number1) + ' ' + str(number2)
    correct_answer = str(find_gcd(number1, number2))
    return question, correct_answer
