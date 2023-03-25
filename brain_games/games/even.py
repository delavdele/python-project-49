from random import randint


general_question = 'Answer "yes" if the number is even, otherwise answer "no".'


def play():
    number = randint(0, 100)
    if number % 2 == 0:
        correct_answer = 'yes'
    else:
        correct_answer = 'no'

    return str(number), correct_answer
