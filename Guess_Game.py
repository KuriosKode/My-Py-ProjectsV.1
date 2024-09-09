# A simple game of guessing...
import random


def guess(g):
    random_number = random.randint(10, g)
    player_guess = 0

    while guess != random_number:
        player_guess = int(input(f"Enter a secret number between 10 and {g} : "))
        if player_guess < random_number:
            print("Your guess is too low!!!")
        elif player_guess > random_number:
            print("Your guess is too High!!!")
        else:
            print("Success , You've guessed the correct number")


guess(50)
