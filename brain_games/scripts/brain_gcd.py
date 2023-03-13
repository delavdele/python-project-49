#!/usr/bin/env python3
from random import randint 
import prompt 
from math import gcd
from brain_games.cli import welcome_user

def num():
    f_num = randint(0, 100)
    s_num = randint(0, 100)
    two_nums = f'{f_num} {s_num}'
    result = gcd(f_num, s_num)
    
    return two_nums, result 

def main():
    print('Welcome to the Brain Games!')
    name = welcome_user()
    print('Find the greatest common divisor of given numbers.')
    success = 0
    for tries in range(0, 3):
        two_nums, result = num()
        print(f"Question: {two_nums}")
        answer = prompt.string("Your answer: ")
        if result == int(answer):
            print("Correct!")
            success += 1 
        else:
            print(f'"{answer}" is wrong answer ;(. Correct answer was "{result}".\nLet\'s try again, {name}!')
            break
  
    if success == 3:
        print(f'Congratulations, {name}!')

if __name__ == '__main__':
    main()
