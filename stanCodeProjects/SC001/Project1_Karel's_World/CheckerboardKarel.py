"""
File: CheckerboardKarel.py
Name: William
----------------------------
When you finish writing it, CheckerboardKarel should draw
a checkerboard using beepers, as described in Assignment 1. 
You should make sure that your program works for all of the 
sample worlds provided in the starter folder.
"""

from karel.stanfordkarel import *


def turn_right():
    """
    Karel will turn left 3 times.
    """
    for i in range(3):
        turn_left()


def turn_around():
    """
    When Karel finish even-line, it will turn left first,
    move one time, and turn left again to get ready for doing odd-line again.
    Pre-condition : Karel is at the bottom of a even-line, facing South.
    Post-condition : Karel is at bottom of a odd-line, facing North.
    """
    turn_left()
    move()
    turn_left()


def fill_odd_line():
    """
    Karel will face North,when it want to fill odd-line's beepers everytime.
    After doing this function, Karel will face East to ready for doing even-line.
    Pre-condition : Karel is at bottom of a odd-line, facing North.
    Post-condition : Karel is at the top of a odd-line, facing East.
    """
    put_beeper()
    while front_is_clear():
        move()
        while front_is_clear():
            move()
            put_beeper()
            if front_is_clear():
                move()
    turn_right()


def check_and_fill_even_line():
    """

    In this function, Karel will check and depend on
    whether odd-line's last position have a beeper to determine
    put beeper on the even-line's first position or not and then
    finish filling even-line.

    Pre-condition : Karel is at the top of a odd-line, facing East.
    Post-condition : Karel is at the bottom of a even-line, facing South.
    """
    if not front_is_clear():
        pass
    else:

        if on_beeper():
            move()
            turn_right()
            if front_is_clear():
                move()
                put_beeper()
                while front_is_clear():
                    move()
                    while front_is_clear():
                        move()
                        put_beeper()
                        if front_is_clear():
                            move()
        else:
            move()
            turn_right()
            put_beeper()
            while front_is_clear():
                move()
                while front_is_clear():
                    move()
                    put_beeper()
                    if front_is_clear():
                        move()


def main():
    """
    Karel will use the functions I created above to
    fulfill all the lines with beepers.
#     And I also set conditions for each function below to ensure that
#     this coding will work in different size of Karel's world.
#     """
    turn_left()
    if not front_is_clear():
        turn_right()
        fill_odd_line()
    while front_is_clear():
        fill_odd_line()
        if front_is_clear():
            check_and_fill_even_line()
        if left_is_clear():
            turn_around()


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
    execute_karel_task(main)
