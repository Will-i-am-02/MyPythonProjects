"""
File: hailstone.py
Name:William
-----------------------
This program should implement a console program that simulates
the execution of the Hailstone sequence, defined by Douglas
Hofstadter. Output format should match what is shown in the sample
run in the Assignment 2 Handout.
"""
# This number will stop the Hailstone Sequences.
EXIT = 1


def main():
    """
    This program will use Hailstone sequence to make the number user enter reach 1.
    """
    print('This program computes Hailstone Sequences')
    print("")
    num = int(input('Enter a number: '))
    times = 0
    if num == EXIT:
        print('It took '+str(times)+' steps to reach 1')
    else:
        while True:
            if num == EXIT:
                break
            if num % 2 == 0:
                print(str(num)+' is even, ', end="")
                num = int(num/2)
                print('so I take half: '+str(num))
                times += 1
            elif num % 2 == 1:
                print(str(num)+' is odd, ', end="")
                num = int(3*num+1)
                print('so I make 3n+1: '+str(num))
                times += 1
        print('It took '+str(times)+' steps to reach 1')


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == "__main__":
    main()
