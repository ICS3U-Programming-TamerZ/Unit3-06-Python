#!/usr/bin/env python3

# Created By: Tamer Zreg
# Date: Oct. 17, 2022
# This program checks if the user guessed a number correctly
# using an If.. Then.. Else statement. Also uses a try-catch statement
# to handle exceptions.

import random


def main():

    # Assigns a random number from 0-9 to the secret_number variable.
    secret_number = random.randint(0, 9)

    # Requests the user's guess.
    print("The secret number is within the range of 0-9")
    user_guess = input("Enter your guess: ")

    # Tries casting user_guess from string to int.
    try:
        user_guess = int(user_guess)

    # Code executed if user_guess cannot be converted to int.
    except ValueError:
        print("You did not enter an integer.")

        # Loops through code until user_guess is an integer
        while not isinstance(user_guess, int):
            print("The secret number is within the range of 0-9")
            user_guess = input("Enter your guess: ")

            # Tries casting user_guess from string to int.
            try:
                user_guess = int(user_guess)

                # If user_guess is an integer, the loop is broken
                break
            except ValueError:
                print("Please try again.")

    # Code executed if the user guessed correctly.
    if secret_number == user_guess:
        print("You guessed correctly!")

    # Code executed if the user guessed incorrectly.
    else:
        print(f"You guessed incorrectly. The correct answer was {secret_number}")


if __name__ == "__main__":
    main()
