import brain_games.engine
from random import randint
import prompt

def prime(num):
    for number in range(2, num - 1):
        if num % number == 0:
            return False
    print(num) 
    return True 

    print('Answer "yes" if the number is prime, otherwise answer "no".')
    success = 0
    for tries in range(0, 3):
        num = randint(1, 100)
        result = prime(num)
        print(f"Question: {num}")
        answer = prompt.string('Your answer: ')
        if answer == 'yes':
            if result == True: 
                print('Correct!')
                success += 1
            else:
                print(f'"no" is wrong answer ;(. Correct answer was "yes".\nLet\'s try again, {name}!')
                break
        else:
            if result == False:
                print('Correct!')
                success += 1
            else:
                print(f'"yes" is wrong answer ;(. Correct answer was "no".\nLet\'s try again, {name}!')
                break

    if success == 3:
        print(f'Congratulations, {name}!')
