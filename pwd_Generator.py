# A simple password generator...

import string  # importing string library
import random  # importing random module


def gen_password(min_length, nums=True, special_chars=True):
    letters = string.ascii_letters
    digits = string.digits
    special = string.punctuation
    # getting letters, numbers and special characters

    characters = letters
    if nums:
        characters += digits
        # if numbers , then add numbers to the character string
    if special_chars:
        characters += special
        # if special characters,then add numbers to the character string

    pwd = ""
    meets_criteria = False
    has_number = False
    has_special = False
    # verifying if the password has numbers or not by currently making it false.

    while not meets_criteria or len(pwd) < min_length:
        new_chars = random.choice(characters)
        pwd += new_chars

        if new_chars in digits:
            has_number = True
        elif new_chars in special:
            has_special = True

        meets_criteria = True
        if nums:
            meets_criteria = has_number
        if special_chars:
            meets_criteria = meets_criteria and has_special

    return pwd


# Getting user input
min_length = int(input("Enter the minimum length ..."))
has_number = input("Do you want to have numbers (y/n)").lower() == "y"
has_special = input("Do you want to have special characters (y/n) ").lower() == "y"
pwd = gen_password(min_length, has_number, has_special)  # invoking the gen_password function
print(pwd)
