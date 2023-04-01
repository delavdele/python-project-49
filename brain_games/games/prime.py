from random import randint

general_question = (
    'Answer "yes" if given number is prime. '
    'Otherwise answer "no".'
)


def is_prime(question):
    for number in range(2, question - 1):
        if question % number == 0:
            return False

    return True


def get_question_and_answer():
    question = randint(1, 100)

    return str(question), 'yes' if is_prime(question) else 'no'
