"""
File: coin_flip_runs.py
Name:William
-----------------------
This program should simulate coin flip(s)
with the number of runs input by users.
A 'run' is defined as consecutive results
on either 'H' or 'T'. For example, 'HHHHHTHTT'
is regarded as a 2-run result.
Your program should stop immediately after your
coin flip results reach the number of runs!
"""

import random


def flip():
    """
    This function is used to get a random result to be a game's answer.
    After use this function, it will return "H" or "T" with str data type.
    """
    num = random.choice(range(2))
    if num == 0:
        return "H"
    elif num == 1:
        return "T"


def main():
    """
    This program should simulate coin flip(s)
    with the number of runs input by users.
    A 'run' is defined as consecutive results
    on either 'H' or 'T'. For example, 'HHHHHTHTT'
    is regarded as a 2-run result.
    Your program should stop immediately after your
    coin flip results reach the number of runs!
    """
    print("Let's flip a coin!")
    num_run = int(input('Number of run: '))
    times = 0
    is_in_a_row = False
    run1 = flip()
    flip_times = run1
    while True:
        if times == num_run:
            break
        run2 = flip()
        if run1 == run2:
            if not is_in_a_row:
                times += 1
                is_in_a_row = True
            else:
                is_in_a_row = False
        run1 = run2
        flip_times += run1
    print(flip_times)


# ---- DO NOT EDIT CODE BELOW THIS LINE ---- #

if __name__ == "__main__":
    main()
