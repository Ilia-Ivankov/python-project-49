from brain_games.games.brain_even_logic import rules
from brain_games.games.brain_even_logic import get_question_and_correct_answer
from brain_games.main_logic import run_game


def main():
    run_game(rules, get_question_and_correct_answer)


if __name__ == '__main__':
    main()
