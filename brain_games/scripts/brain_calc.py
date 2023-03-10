#!/usr/bin/env python3

from random import randint
from random import choice 
from brain_games.cli import welcome_user
import prompt


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


def main():
    print('Welcome to the Brain Games!')
    name = welcome_user()
    print('What is the result of the expression?')
    success = 0
    for tries in range(0, 3):
        expression, result = calc()
        print(f"Question: {expression}")
        answer = prompt.string('Your answer: ')
        if result == int(answer):
             print('Correct!')
             success += 1
        else:
             print(f'"{answer}" is wrong answer ;(. Correct answer was "{result}".\nLet\'s try again, {name}!')
             break

    if success == 3:
        print(f'Congratulations, {name}!')

     
if __name__ == '__main__':
    main()
