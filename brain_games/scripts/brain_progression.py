#!/usr/bin/env python3

from brain_games.cli import welcome_user
from random import randint
import prompt

def main():
    f_num = randint(0, 10)
    s_num = randint(0, 10)
    for i in range(1, 11):
        num1 = f_num + (i - 1) * s_num
        result = num1
        print(result, sep=' ', end=' ')        
    print('\n')

if __name__ == '__main__':
    main()
