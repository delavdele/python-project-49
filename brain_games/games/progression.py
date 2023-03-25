from random import randint
from random import randrange

general_question = 'What number is missing in the progression?'


def play():
    f_num = randint(1, 10)
    s_num = randint(1, 10)
    random_index = randrange(1, 11)
    answer = 0
    question = ''
    for i in range(1, 11):
        num1 = f_num + (i - 1) * s_num
        if random_index == i:
            question += '.. '
            answer = num1
        else:
            question += str(num1) + ' '
    return question, str(answer)
