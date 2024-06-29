"""
File: rocket.py
Name:William
-----------------------
This program should implement a console program
that draws ASCII art - a rocket.
The size of rocket is determined by a constant
defined as SIZE at top of the file.
Output format should match what is shown in the sample
run in the Assignment 3 Handout.

"""

# This constant determines rocket size.
SIZE = 10


def head():
    """
    This function use for loop with range
    which is depend on "SIZE" to built a rocket's head part.
    """
    for i in range(SIZE):
        for j in range(SIZE-i):
            print(' ', end="")
        for j in range(i+1):
            print("/", end="")
        for j in range(i+1):
            print("\\", end="")
        print('')


def belt():
    """
    This function use for loop with range
    which is depend on "SIZE" to built a rocket's belt part.
    """
    print("+", end="")
    for i in range(SIZE):
        print('==', end="")
    print('+')


def upper():
    """
    This function use for loop with range
    which is depend on "SIZE" to built a rocket's upper body part.
    """
    for i in range(SIZE):
        for j in range(SIZE-i):
            if j == 0:
                print('|', end="")
            else:
                print('.', end="")
        for j in range(i+1):
            if j % 2 == 0:
                print('/', end="")
            else:
                print('\\', end="")
        for j in range(i+1):
            if (i+j) % 2 == 0:
                print('\\', end="")
            else:
                print('/', end="")
        for j in range(SIZE-i):
            if j == SIZE-i-1:
                print('|', end="")
            else:
                print('.', end="")
        print('')


def lower():
    """
    This function use for loop with range
    which is depend on "SIZE" to built a rocket's lower body part.
    """
    for i in range(SIZE):
        for j in range(i+1):
            if j == 0:
                print('|', end="")
            else:
                print('.', end="")
        for j in range(SIZE-i):
            if j % 2 == 0:
                print('\\', end="")
            else:
                print('/', end="")
        for j in range(SIZE-i):
            if SIZE % 2 == 1:
                if (i+j) % 2 == 0:
                    print('/', end="")
                else:
                    print('\\', end="")
            else:
                if (i+j) % 2 == 0:
                    print('\\', end="")
                else:
                    print('/', end="")
        for j in range(i+1):
            if j == i:
                print('|', end="")
            else:
                print('.', end="")
        print('')


def main():
    """
    This program can draw a rocket at console in different size
    when "SIZE" number at the top of file is different.
    """
    head()
    belt()
    upper()
    lower()
    belt()
    head()


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == "__main__":
    main()
