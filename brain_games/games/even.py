imort brain_games.engine 
from random import randint
import prompt

def even():
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


