#!/usr/bin/env python3

from brain_games.cli import welcome_user
from random import randint


def main():
    print('Welcome to the Brain Games!')
    welcome_user()
    print(randint(0, 100))

if __name__ == '__main__':
    main()
