"""
Have a look at the script called 'human-guess-a-number.py' (in the same folder as this one).

Your task is to invert it: You should think of a number between 1 and 100, and the computer 
should be programmed to keep guessing at it until it finds the number you are thinking of.

At every step, add comments reflecting the logic of what the particular line of code is (supposed 
to be) doing. 
"""

from random import randint

low = 1
high = 100

while True: #while the number wasn't found
    guess = randint(low, high)
    print(f"computer guess: {guess}") #number chosen by the computer
    resp = input("hint (lower/higher/correct): ")
    if resp== "correct":  # answers and appropriaely assigning the guess ranges (low/high)
        print(f"number found: {guess}")
        break
    elif resp == "lower":
        high = guess - 1
    elif resp == "higher":
        low = guess + 1
