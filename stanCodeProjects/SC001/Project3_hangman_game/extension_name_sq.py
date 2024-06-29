"""
File: name_sq.py (extension)
Name: 
----------------------------
This program is an extension of assignment3!
It will ask the user to provide a name, 
and the square pattern of the given name 
will be printed on the console.
"""


def main():
    """
    This program will ask the user to provide a name,
    and then print out this name in a square pattern on the console
    by using functions below defined in this program.
    """
    print('This program prints a name in a square pattern!')
    name = input('Name: ')
    print(name)   # ------------------------->name square's head.
    square(name)  # ------------------------->name square's left and right line.
    print(reverse(name))  # ----------------->name square's bottom.


def square(name):
    """
    :param name: str, a string entered by user.

    This function will print "name"'s words in a square shape(left line & right line)
    form second index to "name"'s last index-1.
    """
    for i in range(len(name)-2):
        for j in range(len(name)):
            if j == 0:
                print(name[i+1], end='')
            elif j == len(name)-1:
                print(name[len(name)-i-2])
            else:
                print(' ', end='')


def reverse(name):
    """
    :param name: str, a string entered by user.
    :return flip: str, a string that reverse 'name'.

    This function will reverse the string user entered which is called 'name'
    """
    filp = ''
    for i in range(len(name)):
        filp = name[i] + filp
    return filp


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
    main()
