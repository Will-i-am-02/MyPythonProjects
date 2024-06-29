"""
File: complement.py
Name:William
----------------------------
This program uses string manipulation to
tackle a real world problem - finding the
complement strand of a DNA sequence.
THe program provides different DNA sequence as
a python string that is case-sensitive.
Your job is to output the complement of them.
"""


def main():
    """
    This program will use the function below
    called "built_complement(dna)" to
    return complement DNA.
    """
    print(build_complement('ATC'))
    print(build_complement(''))
    print(build_complement('ATGCAT'))
    print(build_complement('GCTATAC'))


def build_complement(dna):
    """
    :param dna : str, a string entered by user.
    :return complement : str, return a string store complementary DNA.

    This function can return complementary DNA
    when user built an original DNA string.

    while original DNA string equals to ''(empty string),
    the function will return 'DNA strand is missing.'.
    """
    if dna == '':
        return 'DNA strand is missing.'
    else:
        complement = ''
        for i in range(len(dna)):
            if dna[i] == 'A':
                complement += 'T'
            elif dna[i] == 'T':
                complement += 'A'
            elif dna[i] == 'G':
                complement += 'C'
            else:
                complement += 'G'
        return complement


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
    main()
