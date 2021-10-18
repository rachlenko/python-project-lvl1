#!/usr/bin/env python

import random
import prompt
import sys 
import cli 

def main():
    username = cli.welcome_user()
    print("What number is missing in this progression?")
    # initialization
    questions_round = 3
    correct_answers = 0
    round_number = 0

    # rounds loop
    while round_number < questions_round:

        count_decor = 0
        str_progression = ""
        for i in gen_progression():
            if count_decor == 2:
                str_progression = f"{str_progression} .. "
                generated_answer = i
            else:
                str_progression = f"{str_progression} {i}"
            count_decor += 1

        user_answer = prompt.string(f"Question: {str_progression}\n") 
        print(f"Your answer: {user_answer}")

        check_answer(user_answer, generated_answer, username):
        round_number += 1

    return summary(correct_answers, questions_round, username)


def gen_progression():
    min_step_size = 1
    max_step_size  = 15 
    min_results_in_array = 10 
    max_range_value = 250
    min_range_value = max_step_size * min_results_in_array 
    step = random.randrange(min_step_size,max_step_size)
    start_number = random.randrange(min_range_value, max_range_value)

    tmp_array = []
    for i in range(0, start_number, step):
        tmp_array.append(i)
    #return last 8 results 
    return tmp_array[-8:]


def check_answer(user_answer, generated_answer, username):

    if int(generated_answer) == int(user_answer):
        print("Correct!")
        return True
    else:
        print(
            f""" '{user_answer}' is wrong answer ;( 
                Correct answer was {generated_answer}. """
        )
        print(f"Let's try again, {username}!")
        sys.os.exit()


def summary(correct_answers, questions_round, username):
    missed_answers = 0
    if correct_answers == questions_round:
        print(f"Congratulations, {username}!")
    else:
        missed_answers = questions_round - correct_answers
        print("\n\nGame over")
    return (correct_answers, missed_answers)


if "__main__" == __name__:
    main()
