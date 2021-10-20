#!/usr/bin/env python

import prompt
import random
from brain_games.scripts import cli
import sys

def main():
    rounds = 3
    min_number = 0
    max_number = 100
    username = cli.welcome_user()
    print("""Answer "yes" if the number is even, otherwise answer "no".\n""")

    for i in range(0, rounds):
        number = 73 #random.randrange(min_number, max_number)
        answer = prompt.string(f"Question: {number}\n")
        print(f"Your answer: {answer}")
        correct_anser = get_correct_answer(number)
        if correct_anser != answer:
            print(f"'{answer}' is wrong answer ;( Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {username}!")
            return  
        print("Correct!")
    print(f"Congratulations, {username}!")


def check_answer(answer, number):
    if "yes" in answer: 
        if check_even(number):
            return True
    return False 

def get_correct_answer(num):
    if check_even(num):
        return "yes"
    return "no"

def check_even(number):
    if (number % 2) == 0:
        return True
    
    return False


if __name__ == "__main__":
    main()
