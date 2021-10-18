#!/usr/bin/env python

import prompt
import sys 

def welcome_user():
    print("Welcome to the Brain Games!")
    username  = prompt.string("May I have your name")
    print(f"Hello, {username}") 
    return username

if "__main__" == __name__:
    main()
