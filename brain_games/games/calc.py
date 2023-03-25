from random import randint
from random import choice

general_question = 'What is the result of the expression?'


def play():
    f_num = randint(0, 100)
    s_num = randint(0, 100)
    oper = ['+', '-', '*']
    element = choice(oper)
    result = 0
    expression = ''
    if element == '+':
        expression = f'{f_num} + {s_num}'
        result = f_num + s_num
    elif element == '-':
        expression = f'{f_num} - {s_num}'
        result = f_num - s_num
    elif element == '*':
        expression = f'{f_num} * {s_num}'
        result = f_num * s_num

    return expression, str(result)
