"""
File: extension2_number_checker.py
Name:
------------------------
This program asks our user for input and checks if the input is a
perfect number、deficient number or an abundant number.

A number is said to be perfect if it is equal to the sum of all its
factors (for obvious reasons the list of factors being considered does
not include the number itself).

A number is considered to be abundant if the sum of its factors
(aside from the number) is greater than the number itself.

And a number is said to be deficient if it is bigger than the sum of all its
factors(aside from the number itself).

The program ends when the user enter the EXIT number.
"""
EXIT = -100


def main():
    """
    This program will help user find out if the number user enter is perfect, abundant, or deficient number.
    The program ends when the user enter the EXIT number.
    """
    print('Welcome to the number checker!')
    num = int(input('n: '))
    if num == EXIT:
        print('Have a good one!')
    else:
        while not num == EXIT:
            data = 0  # ---------> To store divisors' sum.
            for i in range(num):
                if i == 0:
                    continue
                if num % i == 0:
                    data = data + i  # Count
            if data == num:
                print(str(num)+' is a perfect number.')
                num = int(input('n: '))
            elif data > num:
                print(str(num) + ' is an abundant number.')
                num = int(input('n: '))
            else:
                print(str(num) + ' is a deficient number.')
                num = int(input('n: '))
        print('Have a good one!')


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
    main()
