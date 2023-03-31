from random import randint
from random import choice
import operator

general_question = 'What is the result of the expression?'


def play():
    first = randint(0, 100)
    second = randint(0, 100)
    operators = [
           ('+', operator.add),
           ('-', operator.sub),
           ('*', operator.mul),
    ]
    oper = choice(operators)
    result = oper[1](first, second)
    expression = f'{first} {oper[0]} {second}'

    return expression, str(result)
