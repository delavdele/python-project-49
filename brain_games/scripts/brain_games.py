#!/usr/bin/env python3

from brain_games.cli import welcome_user
from random import randint
import prompt


def main():
    print('Welcome to the Brain Games!')
    welcome_user()
    print('Answer "yes" if the number is even, otherwise answer "no".')
    for tries in range(0, 3):
        number = randint(0, 100)
        print(f"Question: {number}")
        answer = prompt.string('Your answer: ')
        if number % 2 == 0:
            if answer == 'yes':
                print('Correct!')
            else:
                print('Incorrect!')
        else:
            if number % 2 != 0:
                if answer == 'no':
                    print('Correct!')
                else:
                    print('Incorrect!')
    

#print('Congratulations, Bill!') 
           

if __name__ == '__main__':
    main()
