from random import randint


general_question = 'Answer "yes" if the number is even, otherwise answer "no".'


def get_question_and_answer():
    number = randint(0, 100)

    return str(number), 'yes' if number % 2 == 0 else 'no'
