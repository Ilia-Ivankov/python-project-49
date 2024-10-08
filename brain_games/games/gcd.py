from brain_games.utils import generate_rand_num
from brain_games.constants import GCD_INSTRUCTION
from brain_games.core import run_game
import math


def get_nums_pair_and_answer():
    first_num, second_num = generate_rand_num(), generate_rand_num()
    nums_pair = f'{first_num} {second_num}'
    gcd = math.gcd(first_num, second_num)
    return nums_pair, str(gcd)


def run_gcd_game():
    run_game(get_nums_pair_and_answer, GCD_INSTRUCTION)
