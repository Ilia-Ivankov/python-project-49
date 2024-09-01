from brain_games.constants import PROGRESSION_LENGTH, PROGRESSION_INSTRUCTION
from brain_games.core import run_game
from brain_games.utils import generate_rand_num
from random import randint


def generate_progression(start, step, length):
    return list(range(start, start + step * length, step))


def generate_progression_hidden_num():
    start_num, step = generate_rand_num(), generate_rand_num()
    progression = generate_progression(start_num, step, PROGRESSION_LENGTH)
    index_to_replace = randint(0, PROGRESSION_LENGTH - 1)
    hidden_num = progression[index_to_replace]
    progression[index_to_replace] = '..'
    missed = " ".join(map(str, progression))
    return missed, str(hidden_num)


def run_progression_game():
    run_game(generate_progression_hidden_num, PROGRESSION_INSTRUCTION)
