import prompt
from brain_games.constants import MAX_ROUNDS


def run_game(get_question_and_answer, game_instruction):
    name = prompt.string('Welcome to the Brain Games!\nMay I have your name?')
    print(f'Hello, {name}!\n{game_instruction}')
    for _ in range(MAX_ROUNDS):
        question, correct_answer = get_question_and_answer()
        user_answer = prompt.string(f'Question: {question}\nYour answer: ')
        if user_answer == correct_answer:
            print('Correct!')
        else:
            print(f'"{user_answer}" is wrong answer ;(.'
                  f'Correct answer was "{correct_answer}".\n'
                  f"Let's try again, {name}!")
            return
    print(f'Congratulations, {name}!')
