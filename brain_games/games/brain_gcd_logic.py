from brain_games.utils import generate_rand_num
from brain_games.constants import GCD_INSTRUCTION
from brain_games.core import run_game


def find_gcd(first_number, second_number):
    while first_number != second_number:
        if first_number > second_number:
            first_number -= second_number
        if second_number > first_number:
            second_number -= first_number
    return first_number


def get_gcd_question_and_answer():
    number1, number2 = generate_rand_num(), generate_rand_num()
    question = str(number1) + ' ' + str(number2)
    correct_answer = str(find_gcd(number1, number2))
    return question, correct_answer


def run_gcd_game():
    run_game(get_gcd_question_and_answer, GCD_INSTRUCTION)
