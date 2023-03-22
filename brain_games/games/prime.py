import brain_games.engine
from random import randint
import prompt

general_question = 'Answer "yes" if given number is prime. Otherwise answer "no".'

def play():
    question = randint(1, 100)
    answer = 'yes'    
    for number in range(2, question - 1):
        if question % number == 0:
            answer = 'no'

    return str(question), answer
