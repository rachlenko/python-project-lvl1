#!/usr/bin/env python

import prompt
import random
from brain_games.scripts import cli


def main():
    rounds = 3
    min_number = 0
    max_number = 100
    username = cli.welcome_user()
    print("""Answer "yes" if the number is even, otherwise answer "no".\n""")

    for i in range(0, rounds):
        number = random.randrange(min_number, max_number)
        answer = prompt.string(f"Question: {number}\n")
        print(f"Your answer: {answer}")
        check_answer(answer, number)
    print(f"Congratulations, {username}!")


def check_answer(answer, number):
    if "yes" in answer and check_even(number):
        print("Correct!")
    else:
        print("no")


def check_even(number):
    if (number % 2) == 0:
        return True
    else:
        return False


if __name__ == "__main__":
    main()
