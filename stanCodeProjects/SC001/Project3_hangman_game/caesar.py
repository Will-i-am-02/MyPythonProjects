"""
File: caesar.py
Name:William
------------------------------
This program demonstrates the idea of caesar cipher.
Users will be asked to input a number to produce shifted
ALPHABET as the cipher table. After that, any strings typed
in will be encrypted.
"""


# This constant shows the original order of alphabetic sequence.
ALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'


def main():
    """
    This program will translate the ciphered string
    into deciphered string with secret number which is telling
    you how many times you have to move "ALPHABET" and make "ALPHABET" to"new_alphabet"
    then print out to console.
    """
    new_alphabet = wrap_around()
    ciphered = input("What's the ciphered string ?")
    print(trans(ciphered, ALPHABET, new_alphabet))


def wrap_around():
    """
    This function will turn ALPHABET into new_alphabet
    by move "secret_number" times then return new_alphabet.
    """
    secret_number = int(input('Secret number: '))
    new_alphabet = ''
    new_alphabet += ALPHABET[len(ALPHABET)-secret_number:]
    new_alphabet += ALPHABET[:len(ALPHABET)-secret_number]
    return new_alphabet


def trans(ciphered, ALPHABET, new_alphabet):
    """
    This function will check if ciphered string is all upper first
    then change lower part into upper.

    After change the string into upper, this function will find new_ciphered's
    each place in new_alphabet then translate with ALPHABET's part.
    """
    new_ciphered = ''
    for i in range(len(ciphered)):
        if ciphered[i].isupper():
            new_ciphered += ciphered[i]
        else:
            new_ciphered += ciphered[i].upper()
    deciphered = ''
    for i in range(len(new_ciphered)):
        if new_ciphered[i] not in new_alphabet:
            deciphered += new_ciphered[i]
        else:
            j = new_alphabet.find(new_ciphered[i])
            deciphered += ALPHABET[j]
    return 'The deciphered string is: '+deciphered


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
    main()
