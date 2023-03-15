#!/usr/bin/env python3

from brain_games.cli import welcome_user
from random import randint
from random import randrange
import prompt
from brain_games.cli import welcome_user

def progression():
    f_num = randint(0, 10)
    s_num = randint(0, 10)
    random_index = randrange(1, 11)
    none_object = 0
    for i in range(1, 11):
        num1 = f_num + (i - 1) * s_num 
        if random_index == i:             
            print('..', end=' ')
            none_object = num1 
        else:
            print(num1, sep=' ', end=' ')        
    print('\n')
    return num1

def main():
    print('Welcome to the Brain Games!')
    name = welcome_user()
    print('What number is missing in the progression?')
    success = 0
    for tries in range(0, 3):
        result = progression() 
        print(f"Question: {result}")
        answer = prompt.string("Your answer: ")
        if result == int(answer):
            print("Correct!")
            success += 1 
        else:
            print(f'"{answe}" is wrong answer ;(. Correct answer was "{result}".\nLet\'s try again, {name}!')
            break 

    if success == 3:
        print(f'Congratulations, {name}!')
 
if __name__ == '__main__':
    main()
