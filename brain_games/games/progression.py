import brain_games.engine
from random import randint
from random import randrange
import prompt

def progression():
    f_num = randint(1, 10)
    s_num = randint(1, 10)
    random_index = randrange(1, 11)
    none_object = 0
    for i in range(1, 11):
        num1 = f_num + (i - 1) * s_num 
        if random_index == i:             
            print('..', end=' ')
            none_object = num1 
        else:
            print(num1, end=' ')
    print()        
    return none_object 

    print('What number is missing in the progression?')
    success = 0
    for tries in range(0, 3): 
        print("Question:", end=' ')
        result = progression()
        answer = prompt.string("Your answer: ")
        if result == int(answer):
            print("Correct!")
            success += 1
        else:
            print(f'"{answer}" is wrong answer ;(. Correct answer was "{result}".\nLet\'s try again, {name}!')
            break 

    if success == 3:
        print(f'Congratulations, {name}!')