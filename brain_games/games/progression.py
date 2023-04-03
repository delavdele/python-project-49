from random import randint

general_question = 'What number is missing in the progression?'


def get_question_and_answer():
    start = randint(1, 11)
    step = randint(1, 11)
    stop = start + 10 * step
    random_ind = randint(0, 10)
    answer = 0
    index = 0
    question = ''
    for number in range(start, stop, step):
        if index == random_ind:
            question += '.. '
            answer = number
        else:
            question += str(number) + ' '
        index += 1

    return question.strip(), str(answer)
