import random
from brain_games.constants import MIN_PROGRESSION_LENGTH
from brain_games.constants import MAX_PROGRESSION_LENGTH
from brain_games.constants import PROGRESSION_INSTRUCTION
from brain_games.core import run_game
from brain_games.utils import generate_rand_num


def create_progression(length_of_progression):
    step_progression = generate_rand_num()
    progression = []
    first_number_of_progression = generate_rand_num()
    for _ in range(length_of_progression):
        progression.append(str(first_number_of_progression))
        first_number_of_progression += step_progression
    return progression


def get_progression_question_and_answer():
    progression_length = random.randint(MIN_PROGRESSION_LENGTH,
                                        MAX_PROGRESSION_LENGTH)
    progression = create_progression(progression_length)
    missed_number = random.randint(0, progression_length - 1)
    correct_answer = progression[missed_number]
    correct_answer = str(correct_answer)
    progression[missed_number] = ".."
    question = ' '.join(progression)
    return question, correct_answer


def run_progression_game():
    run_game(get_progression_question_and_answer, PROGRESSION_INSTRUCTION)
