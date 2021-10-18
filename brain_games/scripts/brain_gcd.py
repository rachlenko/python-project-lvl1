#!/usr/bin/env python

import prompt
import random
from brain_games.scripts import cli


def main():
    rounds = 3
    min_number = 0
    max_number = 100
    username = cli.welcome_user()
    print("""Find the greatest common divisor of given numbers.\n""")

    for i in range(0, rounds):
        a = random.randrange(min_number, max_number)
        b = random.randrange(min_number, max_number)
        answer = prompt.string(f"Question: {a} {b} \n")
        print(f"Your answer: {answer}")
        check_answer(answer, calculate_gcd(a, b), username)
    print("Congratulations, Sam!")


def calculate_gcd(a, b):
    if b == 0:
        return a
    return calculate_gcd(b, a % b)


def check_answer(answer, result_number, username):
    if answer == result_number:
        print("Correct!")
        return True
    else:
        print(
            f"""''{answer}'is wrong answer ;(. Correct answer was '{result_number}' """
        )
        print("Let's try again, {username}")
        return False


if __name__ == "__main__":
    main()
