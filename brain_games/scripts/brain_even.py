import prompt
import random 


MAX_ROUNDS = 3
rules = 'Answer "yes" if the number is even, otherwise answer "no".'
def greeting():
    user_name = prompt.string('Welcome to the Brain Games\nMay I have your name?')
    print(f'Hello, {user_name}!')
    if user_name is not None:
        return f'{rules}', user_name  # Return the rules and user_name


def get_number_and_correct_answer(start = 0, end = 1000):
    number = random.randint(start, end)
    correct_answer = 'yes' if number % 2 == 0 else 'no'
    return number, correct_answer


def main():
    rules_text, user_name = greeting()  # Receive the returned values
    print(rules_text) 
    for _ in range(MAX_ROUNDS):
        number, correct_answer = get_number_and_correct_answer() 
        user_answer = prompt.string(f'Question: {number}\nYour answer:')
        if user_answer == correct_answer:
            print('Correct!')
        else:
            print(f'{user_answer} is wrong answer ;(. Correct answer was {correct_answer}.')
            print(f"Let's try again, {user_name}!")
            return
    return f'Congratulations, {user_name}!'


if __name__ == '__main__':
    main()


                

        
