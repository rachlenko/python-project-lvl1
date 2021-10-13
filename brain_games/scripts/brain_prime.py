#!/usr/bin/env python

import prompt
import random


def main():
    rounds = 3
    min_number = 0
    max_number = 100
    print("Welcome to the Brain Games!")
    username = prompt.string("May I have your name \n")
    print(f"Hello {username}!")
    print("""Answer "yes" if given number is prime. Otherwise answer "no"..\n""")

    for i in range(0, rounds):
        number = random.randrange(min_number, max_number)
        answer = prompt.string(f"Question: {number}\n")
        print(f"Your answer: {answer}")
        check_answer(answer, number)
    print("Congratulations, Sam!")


def check_answer(answer, number):
    if "yes" in answer and check_prime(number):
        print("Correct!")
    else:
        print("no")


def check_prime(n):
    if n == 2 or n == 3:
        return True
    if n % 2 == 0 or n < 2:
        return False
    for i in range(3, int(n ** 0.5) + 1, 2):  # only odd numbers
        if n % i == 0:
            return False
    return True


if __name__ == "__main__":
    main()
