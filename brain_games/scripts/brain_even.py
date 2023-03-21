#!/usr/bin/env python3

from random import randint
from brain_games.cli import welcome_user
import prompt
from brain_games.engine import run_game
from brain_games.games.even import play



def main():
    print('Welcome to the Brain Games!')
    name = welcome_user()
    print('Answer "yes" if the number is even, otherwise answer "no".')
    success = 0
    for tries in range(0, 3):
        number = randint(0, 100)
        print(f"Question: {number}")
        answer = prompt.string('Your answer: ')
        if number % 2 == 0:
            if answer == 'yes':
                print('Correct!')
                success += 1
            else:
                print(f'"no" is wrong answer ;(. Correct answer was "yes".\nLet\'s try again, {name}!')
                break
        else:
            if number % 2 != 0:
                if answer == 'no':
                    print('Correct!')
                    success += 1
                else:
                    print(f'"yes" is wrong answer ;(. Correct answer was "no".\nLet\'s try again, {name}!')
                    break

    if success == 3:
        print(f'Congratulations, {name}!')




def start():
    run_game(play)
    
if __name__ == '__main__':
    main()



