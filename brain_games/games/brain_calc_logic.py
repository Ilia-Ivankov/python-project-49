import random
from brain_games.constants import CALC_INSTRUCTION
from brain_games.core import run_game
from brain_games.utils import generate_rand_num
from brain_games.constants import MATH_SYMBOLS


def get_random_math_sign_and_result(first_number, second_number, sign):
    match sign:
        case "+":
            result = first_number + second_number
        case "-":
            result = first_number - second_number
        case "*":
            result = first_number * second_number
    return result


def get_math_question_and_result():
    number1, number2 = generate_rand_num(), generate_rand_num()
    math_sign = random.choice(MATH_SYMBOLS)
    question = f'{number1} {math_sign} {number2}'
    correct_answer = str(eval(question))
    return question, correct_answer


def run_calc_game():
    run_game(get_math_question_and_result, CALC_INSTRUCTION)
