"""
File: anagram.py
Name:William
----------------------------------
This program recursively finds all the anagram(s)
for the word input by user and terminates when the
input string matches the EXIT constant defined
at line 19

If you correctly implement this program, you should see the
number of anagrams for each word listed below:
    * arm -> 3 anagrams
    * contains -> 5 anagrams
    * stop -> 6 anagrams
    * tesla -> 10 anagrams
    * spear -> 12 anagrams
"""

import time                   # This file allows you to calculate the speed of your algorithm

# Constants
FILE = 'dictionary.txt'       # This is the filename of an English dictionary
EXIT = '-1'                   # Controls when to stop the loop


def main():
    """
    TODO:
    """
    print('Welcome to stanCode "Anagram Generator" (or -1 to quit)')
    word = input('Find anagrams for: ')
    if word == EXIT:
        print('Bye!')
    else:
        while True:
            if word == EXIT:
                print('Bye!')
                break
            print('Searching...')
            found_lst = find_anagrams(word)
            print(f'{len(found_lst)} anagrams: {found_lst}')
            word = input('Find anagrams for: ')

    # start = time.time()
    # ####################
    # #                  #
    # #       TODO:      #
    # #                  #
    # ####################
    # end = time.time()
    # print('----------------------------------')
    # print(f'The speed of your anagram algorithm: {end-start} seconds.')


def read_dictionary():
    with open(FILE, 'r') as f:
        all_words = []
        for line in f:
            all_words.append(line[:-1])
    return all_words


def find_anagrams(s):
    """
    :param s:
    :return:
    """
    found_lst = find_anagrams_helper(s, "", len(s), [])
    return found_lst


def find_anagrams_helper(s, current_s, ans_len, store):
    all_words = read_dictionary()
    if len(current_s) == ans_len:
        if current_s in all_words:
            store.append(current_s)
            print(f'Found: {current_s}')
            print('Searching...')
        return store
    else:
        for word in s:
            if word in current_s:
                pass
            else:
                # Choose
                current_s += word
                # Explore
                find_anagrams_helper(s, current_s, ans_len, store)
                # Un-choose
                current_s = current_s[:-1]


def has_prefix(sub_s):
    """
    :param sub_s:
    :return:
    """
    pass


if __name__ == '__main__':
    main()
