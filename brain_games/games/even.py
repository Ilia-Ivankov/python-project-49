from brain_games.utils import generate_rand_num
from brain_games.constants import EVEN_INSTRUCTION
from brain_games.core import run_game


def is_even(number):
    return number % 2 == 0


def get_even_question_and_correct_answer():
    question = generate_rand_num()
    correct_answer = 'yes' if is_even(question) else 'no'
    return question, correct_answer


def run_even_game():
    run_game(get_even_question_and_correct_answer, EVEN_INSTRUCTION)
