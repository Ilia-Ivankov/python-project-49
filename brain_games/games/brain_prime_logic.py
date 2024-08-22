from brain_games.utils import generate_rand_num
from brain_games.constants import PRIME_INSTRUCTION
from brain_games.core import run_game


def is_prime(number):
    k = 2
    while k != number:
        if number % k == 0:
            return False
        else:
            k += 1
    return k == number


def get_prime_question_and_correct_answer():
    question = generate_rand_num()
    correct_answer = 'yes' if is_prime(question) else 'no'
    return question, correct_answer


def run_prime_game():
    run_game(get_prime_question_and_correct_answer, PRIME_INSTRUCTION)
