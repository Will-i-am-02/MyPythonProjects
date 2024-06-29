"""
File: similarity.py (extension)
Name:William
----------------------------
This program is an extension of assignment3!
It will compare short dna sequence, s2,
with sub sequences of a long dna sequence, s1
The way of approaching this task is the same as
what people are doing in the bio industry.
"""


def main():
    """
    This program will ask user to provide long DNA sequence
    and short DNA sequence.
    After user entered two DNA sequences,
    the program will compare this two DNA sequences' most matchable part, then print out this part.

    """
    long = input('Please give me a DNA sequence to search: ')
    short = input('What DNA sequence would you like to match? ')
    print(match(long, short))


def match(long, short):
    """
    :param long : str, a string store long DNA sequence entered by user.
    :param short : str, a string store short DNA sequence entered by user.
    :return perfect : str, a string store the most matchable part then return.

    This function will compare two DNA sequences' most matchable part,
    then return this part for "main" to print.
    """
    ####################################################
    # This part let this program case-sensitive.
    new_long = ''
    new_short = ''
    for i in range(len(long)):
        if long[i].isupper():
            new_long += long[i]
        else:
            new_long += long[i].upper()
    for i in range(len(short)):
        if short[i].isupper():
            new_short += short[i]
        else:
            new_short += short[i].upper()
    ####################################################

    store = ''         # Use to store the most matchable part, then continue to compare.
    perfect = ''       # let "perfect" equal to each new "store".
    compare = 0        # Use to count how many short DNA string's words are match with long DNA string's.
    perfect_times = 0  # let "perfect_times" equal to each new "compare".

    ####################################################
    # This part compare two DNA sequences' most matchable part.
    for i in range(len(new_long)-len(new_short)+1):
        for j in range(len(new_short)):
            if new_short[j] == new_long[i+j]:
                compare += 1
            store += new_long[i+j]
        if compare > perfect_times:
            perfect_times = compare
            perfect = store
        store = ''
        compare = 0
    ####################################################
    return 'The best match is ' + perfect


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
    main()
