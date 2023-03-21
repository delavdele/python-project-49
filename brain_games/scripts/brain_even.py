#!/usr/bin/env python3

from random import randint
from brain_games.cli import welcome_user
import prompt
from brain_games.engine import run_game
import brain_games.games.even


def start():
    run_game(brain_games.games.even)
    


if __name__ == '__main__':
    main()



