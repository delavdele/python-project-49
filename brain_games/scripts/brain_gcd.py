#!/usr/bin/env python3

from random import randint
from random import choice
from brain_games.cli import welcome_user
import prompt
from brain_games.engine import run_game
import brain_games.games.gcd


def start():
    run_game(brain_games.games.gcd)



if __name__ == '__main__':
    main()
