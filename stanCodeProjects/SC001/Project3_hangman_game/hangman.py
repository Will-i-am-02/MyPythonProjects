"""
File: hangman.py
Name:William
-----------------------------
This program plays hangman game.
Users see a dashed word, trying to
correctly figure the un-dashed word out
by inputting one character each round.
If the user input is correct, show the
updated word on console. Players have N_TURNS
chances to try and win this game.
"""


import random


# This constant controls the number of guess the player has.
N_TURNS = 7


def main():
    """
    This program plays hangman game.
    Users see a dashed word, trying to
    correctly figure the un-dashed word out
    by inputting one character each round.
    If the user input is correct, show the
    updated word on console. Players have N_TURNS
    chances to try and win this game.
    """
    answer = random_word()  # -----> Use random_word() to get a word for answer.
    dash = dashed(answer)   # -----> After answer use dash(ans), use dash to store dashed answer.
    print('The word looks like: '+dash)
    times = N_TURNS
    print('You have ' + str(times) + ' wrong guesses left.')
    while True:
        input_ch = input('Your guess: ')
        dash, times = is_right(input_ch, answer, times, dash)
        if '-' not in dash or times == 0:
            break


def random_word():
    """
    This function is used to get a random word to be a game's answer.
    After use this function, it will return a word with str data type.
    """
    num = random.choice(range(9))
    if num == 0:
        return "NOTORIOUS"
    elif num == 1:
        return "GLAMOROUS"
    elif num == 2:
        return "CAUTIOUS"
    elif num == 3:
        return "DEMOCRACY"
    elif num == 4:
        return "BOYCOTT"
    elif num == 5:
        return "ENTHUSIASTIC"
    elif num == 6:
        return "HOSPITALITY"
    elif num == 7:
        return "BUNDLE"
    elif num == 8:
        return "REFUND"


def dashed(ans):
    """
    Use this function to make string called ans into a string composed of dash.
    Then return this new string.

    :param ans: str, the game use random_word() to get a word to be this game's answer.
    :return dash: str, make ans into a string composed of dash.
    """
    dash = ''
    for i in range(len(ans)):
        dash += '-'
    return dash


def is_right(input_ch, answer, times, dash):
    """
    Use this function can help identfy the character entered by user is right guess, wrong guess,
    or illegal format.


    :param input_ch :str, A character entered by user.
    :param answer : str, This game's answer which is a string use function to get a random word.
    :param times: int, Store user have how many times to guess.
    :param dash: str, It's a string that make each of answer's character into dash.

    :return undash :str, If user's guess is right, return undash.
    :return times :int, Whatever conditions will return times.
    :return dash :str, If user's guess is wrong or illegal, return dash.
    """
    if not input_ch.isalpha():
        print('Illegal format.')
        return dash, times
    if len(input_ch) > 1:
        print('Illegal format.')
        return dash, times
    if not input_ch.isupper():
        upper_ch = input_ch.upper()
    else:
        upper_ch = input_ch
    if upper_ch in answer:
        undash = ''
        # if dash == '':
        #     for i in range(len(answer)):
        #         dash += '-'
        # else:
        #     pass
        for i in range(len(answer)):
            if dash[i] == '-':
                if upper_ch == answer[i]:
                    undash += upper_ch
                elif dash[i] == answer[i]:
                    undash += dash[i]
                else:
                    undash += '-'
            else:
                undash += dash[i]
        if undash == answer:
            print('You are correct!')
            print('You win!!')
            print('The answer is: '+answer)
            return undash, times
        else:
            print('You are correct!')
            print('The word looks like: ' + undash)
            print('You have ' + str(times) + ' wrong guesses left.')
            return undash, times

    else:
        times -= 1
        if times != 0:
            print('There is no '+upper_ch+"'s in the word.")
            print('The word looks like: ' + dash)
            print('You have ' + str(times) + ' wrong guesses left.')
            return dash, times
        else:
            print('There is no ' + upper_ch + "'s in the word.")
            print('You are completely hang :(')
            print('The answer is: ' + answer)
            return dash, times


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
    main()
