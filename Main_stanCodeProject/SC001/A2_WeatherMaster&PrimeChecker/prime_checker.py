"""
File: prime_checker.py
Name: Blair
-----------------------
This program asks our user for input and checks if the input is a
prime number or not. First, ” Welcome to the prime checker” will be printed on Console.
And the program will continually ask the user to enter an integer 
that is greater than 1 and checks if it is a prime number.
The program ends when the user enter the EXIT number.
"""

EXIT = -100


def main():
    """
    Checking whether the numbers entered are prime numbers by keeping dividing each number
    until it's evenly divided.
    """
    print('Welcome to the prime checker! Check the numbers greater than 1.')
    n = int(input('Number to check: ( or ' + str(EXIT) + ' to quit)?'))
    div = 2
    while n != EXIT:
        while n % div != 0:
            div += 1
        if div == n:
            print(str(n) + ' is a prime number.')
        else:
            print(str(n) + ' is not a prime number.')
        # reset div before enter a new number
        div = 2
        n = int(input('Number to check: ( or ' + str(EXIT) + ' to quit)?'))
    print('Have a good one!')


if __name__ == "__main__":
    main()
