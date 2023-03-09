#!/usr/bin/env python3

from random import randint
from random import choice 

def calc():
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

    return expression, result 
     
if __name__ == '__main__':
    main()
