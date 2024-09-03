"""
File: hangman.py
Name: Blair
-----------------------------
This program plays hangman game.
Users see a dashed word, trying to
correctly figure the un-dashed word out
by inputting one character each round.
If the user input is correct, show the
updated word on console. Players have N_TURNS
chances to try and win this game.
"""

import random

# This constant controls the number of guess the player has.
N_TURNS = 7


def main():
    """
    Distinguishing whether the character entered is among the answer.
    The game ends when no life remains, or the answer is guessed.
    """
    lives = N_TURNS
    answer = random_word()
    # Cover the answer with dashes('-')
    ans = ""
    for i in range(len(answer)):
        if answer[i].isalpha():
            ans += "_"
    while lives >= 1 and not ans.isalpha():
        print("The word looks like " + str(ans))
        print("You have " + str(lives) + " wrong guesses left.")
        input_ch = input("Your guess: ")
        # Check the format
        if not input_ch.isalpha() or len(input_ch) != 1:
            print('Illegal Format')
        else:
            # Make it case insensitive
            if input_ch.islower():
                input_ch = input_ch.upper()
            # Start Checking
            if input_ch in answer:
                print("You are correct!")
            else:
                lives -= 1
                print("There is no " + str(input_ch) + "'s in the word.")
            # Update the covered answer
            box = ''
            for i in range(len(answer)):
                if not ans[i].isalpha():
                    if answer[i] == input_ch:
                        box += input_ch
                    else:
                        box += "_"
                else:
                    box += ans[i]
            ans = box
    # Check the result of the game
    if ans.isalpha():
        print("You win!!")
        print("The word was: " + str(ans))
    else:
        print("You are completely hung :(")
        print("The word was: " + str(answer))


def random_word():
    num = random.choice(range(9))
    if num == 0:
        return "NOTORIOUS"
    elif num == 1:
        return "GLAMOROUS"
    elif num == 2:
        return "CAUTIOUS"
    elif num == 3:
        return "DEMOCRACY"
    elif num == 4:
        return "BOYCOTT"
    elif num == 5:
        return "ENTHUSIASTIC"
    elif num == 6:
        return "HOSPITALITY"
    elif num == 7:
        return "BUNDLE"
    elif num == 8:
        return "REFUND"


if __name__ == '__main__':
    main()
