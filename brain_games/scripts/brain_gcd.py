from brain_games.main_logic import run_game
from brain_games.games.brain_gcd_logic import get_question_and_correct_answer
from brain_games.games.brain_gcd_logic import rules


def main():
    run_game(rules, get_question_and_correct_answer)


if __name__ == '__main__':
    main()
