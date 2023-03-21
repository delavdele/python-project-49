#!/usr/bin/env python3

from random import randint
from random import choice 
from brain_games.cli import welcome_user
import prompt
from brain_games.engine import run_game
from brain_games.games.calc import play


def start():
    run_game(play)
    

     
if __name__ == '__main__':
    main()
