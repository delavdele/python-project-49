import prompt
from brain_games.cli import welcome_user


def run_game(game):
    print('Welcome to the Brain Games!')
    name = welcome_user()
    print(game.general_question)
    success = 0
    for tries in range(0, 3):
        question, answer = game.play()
        print(f"Question: {question}")
        user_answer = prompt.string('Your answer: ')
        if answer == user_answer:
            print('Correct!')
            success += 1
        else:
            print(f'"{user_answer}" is wrong answer ;(. Correct answer was "{answer}".\nLet\'s try again, {name}!')
            break

    if success == 3:
        print(f'Congratulations, {name}!')
