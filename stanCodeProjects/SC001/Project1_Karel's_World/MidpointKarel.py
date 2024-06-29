"""
File: MidpointKarel.py
Name: William
----------------------------
When you finish writing it, MidpointKarel shouldb           cxcxgfcdx
leave a beeper on the corner closest to the center of 1st Street
(or either of the two central corners if 1st Street has an even
number of corners).  Karel can put down additional beepers as it
looks for the midpoint, but must pick them up again before it
stops.  The world may be of any size, but you are allowed to
assume that it is at least as tall as it is wide.
"""

from karel.stanfordkarel import *


def turn_around():
    """
    Karel will turn left 2 times.
    """
    for i in range(2):
        turn_left()


def find_mid():
    """

    Karel will use functions I created to find midpoint.
    """
    place_beeper_wall()  # Karel will move to the end and put a beeper at (1, 5) then turn around and move to (1, 4).
    while not on_beeper():
        is_it_mid()
        find_beeper()


def place_beeper_wall():
    """

    Karel will move to the end and put a beeper at (1, 5).
    After doing this Karel will turn around and move to (1, 4)
    to ready for doing next command.
    """
    while front_is_clear():
        move()
    put_beeper()
    turn_around()
    move()


def is_it_mid():
    """

    Karel will find mid via a logical method
    that put beepers from two sides to inside.
    """
    move()
    if on_beeper():
        turn_around()
        move()
        put_beeper()


def find_beeper():
    """
    Karel use this function to help itself to find midpoint
    because the function "is_it_mid" only do once.
    "is_it_mid" will skip to this function to go on finding mid.
    """
    if not on_beeper():
        while not on_beeper():
            move()
        turn_around()
        move()
        put_beeper()
        move()


def remove_all_beepers():
    """
    Karel will pick up all beepers instead of the beeper at midpoint.
    """

    pick_beeper_wall()
    turn_around()
    go_to_mid()
    pick_beeper_wall()
    turn_around()


def go_to_mid():
    """
    After Karel pick up half side of beepers, it need to use this function to back to midpoint.
    Because midpoint's beeper is the first beeper Karel will meet after doing "pick_beeper_wall."
    """
    while not on_beeper():
        move()


def pick_beeper_wall():
    """

    Karel use this function to pick up midpoint's two sides' beepers.
    """
    while front_is_clear():
        move()
        pick_beeper()


def main():
    """
    Karel will find midpoint, put the only one beeper at midpoint,
    and stop at midpoint by using functions I created above.
    """
    put_beeper()  # put first beeper at (1, 1).
    if front_is_clear():
        move()
        if front_is_clear():
            find_mid()
            remove_all_beepers()
            go_to_mid()
        else:
            turn_around()
            go_to_mid()


# DO NOT EDIT CODE BELOW THIS LINE #


if __name__ == '__main__':
    execute_karel_task(main)
