from brain_games.constants import MIN_LENGTH_RAND_NUM
from brain_games.constants import MAX_LENGTH_RAND_NUM
import random


def generate_rand_num():
    return random.randint(MIN_LENGTH_RAND_NUM, MAX_LENGTH_RAND_NUM)
