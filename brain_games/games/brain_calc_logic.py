import random


rules = 'What is the result of the expression?'


def get_question_and_correct_answer(start=0, end=100):
  number1 = random.randint(start, end)
  number2 = random.randint(start, end)
  symbols = ["+","-","*"]
  symbol = random.choice(symbols)
  question = f"{number1} {symbol} {number2}"
  correct_answer = number1 + number2
  match symbol:
      case "+":
          correct_answer = number1 + number2
      case "-":
          correct_answer = number1 - number2
      case "*":
          correct_answer = number1 * number2
  correct_answer = str(correct_answer)
  return question, correct_answer
