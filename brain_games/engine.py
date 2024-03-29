import prompt


def run_game(game):
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print('Hello, ' + name)
    print(game.general_question)
    tries = 3
    for _ in range(0, tries):
        question, answer = game.get_question_and_answer()
        print(f"Question: {question}")
        user_answer = prompt.string('Your answer: ')
        if answer == user_answer:
            print('Correct!')
        else:
            print(f'"{user_answer}" is wrong answer ;(. '
                  f'Correct answer was "{answer}".\n'
                  f'Let\'s try again, {name}!')
            return

    print(f'Congratulations, {name}!')
