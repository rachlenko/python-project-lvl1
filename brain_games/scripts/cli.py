#!/usr/bin/env python

import prompt


def welcome_user():
    print("Welcome to the Brain Games!")
    username = prompt.string("May I have your name? ")
    print(f"Hello, {username}!")
    return username


def main():
    welcome_user()


if "__main__" == __name__:
    main()
