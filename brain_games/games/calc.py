from random import randint
from random import choice
import operator

general_question = 'What is the result of the expression?'


def play():
    first_num = randint(0, 100)
    second_num = randint(0, 100)
    operators = [
           ('+', operator.add),
           ('-', operator.sub),
           ('*', operator.mul),
    ]
    operator_elements = choice(operators)
    result = operator_elements[1](first_num, second_num)
    expression = f'{first_num} {operator_elements[0]} {second_num}'

    return expression, str(result)
