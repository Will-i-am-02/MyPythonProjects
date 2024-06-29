"""
File: extension3_triangular_checker.py
Name:
--------------------------
This program asks our user for input and checks if the input is an
triangular number or not.

The triangular number (Tn) is a number that can be represented in the form of a triangular
grid of points where the first row contains a single element and each subsequent row contains 
one more element than the previous one.

We can just use the fact that the nth triangular number can be found by using a formula: Tn = n(n + 1) / 2.

The program ends when the user enter the EXIT number.
"""
EXIT = -100


def main():
    """
    This program asks our user for input and checks if the input is a
    triangular number or not.
    """
    print('Welcome to the triangular number checker!')
    n = int(input('n: '))
    if n == EXIT:
        print('Have a good one!')
    else:
        while not n == EXIT:
            x = 1
            for i in range(n):
                if x*(x+1)/2 < n:
                    x += 1
                elif x*(x+1)/2 == n:
                    print(str(n) + ' is a triangular number')
                    n = int(input('n: '))
                    break
                else:
                    print(str(n) + ' is not a triangular number')
                    n = int(input('n: '))
                    break
        print('Have a good one!')


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
    main()
