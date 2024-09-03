"""
File: interactive.py
Name: Blair
------------------------
This file uses the function interactivePrompt
from util.py to predict the reviews input by 
users on Console. Remember to read the weights
and build a Dict[str: float]
"""

from util import *
from submission import *


def main():
    weights = {}
    with open('weights', 'r') as f:
        for line in f:
            word, weight = line.split()
            weights[word] = float(weight)

    interactivePrompt(extractWordFeatures, weights)


if __name__ == '__main__':
    main()
