"""
File: extension4_narcissistic_checker.py
Name:William
------------------------
This program asks our user for input and checks if the input is a
narcissistic number or not.

A positive integer is called a narcissistic number if it
is equal to the sum of its own digits each raised to the
power of the number of digits.

Example: 153 is narcissistic because 1^3 + 5^3 + 3^3 = 1 + 125 + 27 = 153.
Note that by this definition all single digit numbers are narcissistic.

Students are recommended to use // and % to complete this program.

The program ends when the user enter the EXIT number.
"""
EXIT = -100


def main():
    """
    This program will continually ask user to enter a number
    and check if the number is a narcissistic number.

    A positive integer is called a narcissistic number if it
    is equal to the sum of its own digits each raised to the
    power of the number of digits.

    Example: 153 is narcissistic because 1^3 + 5^3 + 3^3 = 1 + 125 + 27 = 153.
    Note that by this definition all single digit numbers are narcissistic.
    """

    print('Welcome to the narcissistic number checker!')
    num = int(input('n: '))
    if num == EXIT:
        print('Have a good one!')
    else:
        while not num == EXIT:
            n1 = num
            """
            I use n1 to store the num user enter because 
            in the first while True loop below will make num to zero.
            If the num is zero, the program can't run the second while True loop below.   
            """
            n2 = num
            """
            I use n2 to store the num user enter because
            after run two while True loops below n1 and num
            will be made to zero.
            If n1 and num are zero,the program will let "if asum == n1 or num " always be False.
            That's why I need n2 to store the num user enter.
            """
            i = 0
            """
            I use i to count the digit.
            """
            asum = 0
            """
            I use asum to every digit's number count i times first then add each other.
            """
            while True:
                num = num // 10  # -----> cut digits.
                i += 1
                if num == 0:
                    break
            while True:
                rn = n1 % 10  # -----> rn is use to store digits.
                asum += rn ** i
                n1 = n1 // 10
                if n1 == 0:
                    break
            if asum == n2:
                print(str(n2) + ' is a narcissistic number')
                num = int(input('n: '))
            else:
                print(str(n2) + ' is not a narcissistic number')
                num = int(input('n: '))
        print('Have a good one!')


if __name__ == '__main__':
    main()
