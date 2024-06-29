"""
File: StoneMasonKarel.py
Name: William
--------------------------------
At present, the StoneMasonKarel file does nothing.
Your job in the assignment is to add the necessary code to
instruct Karel to build a column (a vertical structure
that is 5 beepers tall) in each avenue that is either on the right
or left side of the arch, as described in the Assignment 1 handout. 
Karel should end on the last avenue, 1st Street, facing east. 
"""

from karel.stanfordkarel import *


def make_u_turn():
    """
    Karel will turn left 2 times.
    """
    for i in range(2):
        turn_left()


def go_to_next_pillar():
    """
    Karel will move to next pillar.
    """
    for i in range(4):
        move()


def built():
    """
    Karel will fulfill the beepers and then back to its initial position at each pillar's beginning.
    """
    up()
    down()


def up():
    """

    Pre-condition : Karel is at each pillar's beginning, facing East.
    Post-condition : Karel is at each pillar's top, facing North.
    """
    turn_left()
    for i in range(4):
        if on_beeper():
            move()
        else:
            put_beeper()
            move()
    if not on_beeper():
        put_beeper()


def down():
    """

    Pre-condition : Karel is at each pillar's top, facing North.
    Post-condition : Karel is at each pillar's beginning, facing East.
    """
    make_u_turn()

    while front_is_clear():
        move()
    turn_left()


def main():
    """
    Karel use while loop and two functions I created,
    which called "built" and "go_to_next_pillar" to fulfill each pillar with beepers.
    """
    while front_is_clear():
        built()
        go_to_next_pillar()
    built()


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
    execute_karel_task(main)
