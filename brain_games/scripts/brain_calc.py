#!/usr/bin/env python

import prompt
import random
import sys
import cli

def main():
    rounds = 3
    min_number = 0
    max_number = 100
    subtraction = 0
    adding = 1
    multiplication = 2
    username = cli.welcome_user()
    print("""What is the result of the expression? \n""")

    for i in range(0, rounds):

        first_number = random.randrange(min_number, max_number)
        second_number = random.randrange(min_number, max_number)

        if i == subtraction:
            if second_number > first_number:
                a, b = second_number, first_number
            else:
                a, b = first_number, second_number
            answer = prompt.string(f"Question: {a} - {b}\n")
            print(f"Your answer: {answer}")
            check_answer(int(answer), int(a - b), username)

        if i == adding:
            answer = prompt.string(f"Question: {first_number} + {second_number}\n")
            print(f"Your answer: {answer}")
            check_answer(int(answer), int(first_number + second_number), username)

        if i == multiplication:
            answer = prompt.string(f"Question: {first_number} * {second_number}\n")
            print(f"Your answer: {answer}")
            check_answer(int(answer), int(first_number * second_number), username)

    print("Congratulations, Sam!")


def check_answer(answer, number, username):
    if answer == number:
        print("Correct!")
    else:
        print(f""" '{answer}'is wrong answer ;(. Correct answer was {number} """)
        print("Let's try again, {username}")
        sys.exit(1)


def check_even(number):
    if (number % 2) == 0:
        return True
    else:
        return False


if __name__ == "__main__":
    main()
