"""
File: extension1_MidpointKarel.py
Name: William
----------------------------
When you finish writing it, MidpointKarel should
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


def main():
    """
    TODO:
    """
    put_beeper()
    move()
    put_beeper()
    move()
    put_beeper()

# DO NOT EDIT CODE BELOW THIS LINE #


if __name__ == '__main__':
    execute_karel_task(main)
