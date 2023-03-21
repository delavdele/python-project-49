from random import randint
import prompt


def play():
    number = randint(0, 100)
    if number % 2 == 0:
        correct_answer = 'yes'
    else:
        correct_answer = 'no'

    return str(number), correct_answer
    

