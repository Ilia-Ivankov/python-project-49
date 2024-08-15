import prompt


def greeting(rules):
    print('Welcome to the Brain Games!')
    user_name = prompt.string('May I have your name?')
    print(f'Hello, {user_name}!')
    if user_name is not None:
        return f'{rules}', user_name


def run_game(rules, get_question_and_correct_answer, MAX_ROUNDS=3):
    rules_text, user_name = greeting(rules)  # Receive the returned values
    print(rules_text)
    for _ in range(MAX_ROUNDS):
        question, correct_answer = get_question_and_correct_answer()
        user_answer = prompt.string(f'Question: {question}\nYour answer:')
        if user_answer == correct_answer:
            print('Correct!')
        else:
            print(f'"{user_answer}" is wrong answer ;(.'
                  + f'Correct answer was "{correct_answer}".')
            print(f"Let's try again, {user_name}!")
            return 
    print(f'Congratulations, {user_name}!')
