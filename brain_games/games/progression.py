from random import randint
from random import randrange

general_question = 'What number is missing in the progression?'


def get_question_and_answer():
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


def get_question_and_answer():
    start = randint(1, 10)
    step = randint(1, 10)
    stop = start + 10 * step
    random_index = randint(1, 11)
    progression = list(range(start, start + 10 * step, step))
    hidden_number = progression[random_index]
    for n in range(start, stop, step):
