"""
File: CollectNewspaperKarel.py
Name: William
--------------------------------
At present, the CollectNewspaperKarel file does nothing.
Your job in the assignment is to add the necessary code to
instruct Karel to walk to the door of its house, pick up the
newspaper (represented by a beeper, of course), and then return
to its initial position in the upper left corner of the house.
"""

from karel.stanfordkarel import *


def turn_right():
    """
    Karel will turn left 3 times.
    """
    for i in range(3):
        turn_left()


def make_u_turn():
    """
    Karel will turn left 2 times.
    """
    for i in range(2):
        turn_left()


def go_to_pick_paper():
    """

    Pre-condition : Karel is facing East, at the upper left corner of the house.
    Post-condition :Karel is facing East, at Street 3, Avenue 6.
    """

    while front_is_clear():
        move()
    turn_right()
    while not left_is_clear():
        move()
    turn_left()
    move()
    pick_beeper()


def go_home_and_put_paper():
    """

        Pre-condition :Karel is facing East, at Street 3, Avenue 6.
        Post-condition : Karel is facing East, at the upper left corner of the house.
    """
    make_u_turn()
    while front_is_clear():
        move()
    turn_right()
    move()
    turn_right()
    put_beeper()


def main():
    """

    Karel will walk to the door, pick up the newspaper,
    and then back to its initial position in the upper left corner of the house
    by using the two function I created.

    """
    go_to_pick_paper()
    go_home_and_put_paper()


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
    execute_karel_task(main)
