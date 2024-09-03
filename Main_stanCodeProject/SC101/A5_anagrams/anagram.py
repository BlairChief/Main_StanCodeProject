"""
File: anagram.py
Name: Blair
----------------------------------
This program recursively finds all the anagram(s)
for the word input by user and terminates when the
input string matches the EXIT constant

If you correctly implement this program, you should see the
number of anagrams for each word listed below:
    * arm -> 3 anagrams
    * contains -> 5 anagrams
    * stop -> 6 anagrams
    * tesla -> 10 anagrams
    * spear -> 12 anagrams
"""

import time  # This file allows you to calculate the speed of your algorithm

# Constants
FILE = 'dictionary.txt'  # This is the filename of an English dictionary
EXIT = '-1'  # Controls when to stop the loop


def main():
    """
    find all the anagrams of the words input by users
    """
    print('Welcome to stanCode \"Anagram Generator" (or ' + str(EXIT) + ' to quit)')
    word = input('Find anagrams for: ')
    while word != EXIT:
        # start searching
        start = time.time()
        print('Searching...')
        dic = read_dictionary(word)
        # check if the word is in the dictionary
        if dic:
            output = find_anagrams(word, dic)
            print(str(len(output)) + ' anagrams: ' + str(output))
            # end searching
            end = time.time()
            print('----------------------------------')
            print(f'The speed of your anagram algorithm: {end - start} seconds.')
            # word = input('Find anagrams for: ')
        else:
            print('Not in the dictionary')
        word = input('Find anagrams for: ')


def read_dictionary(word):
    """
    :param word: str, the word input by users
    :return dic_words: list[str], the words highly related to the anagrams
    """
    dic_words = []
    with open(FILE, 'r') as f:
        for line in f:
            line = line.strip()
            if len(line) == len(word):
                if word[0] in line and word[-1] in line:
                    if set(line) == set(word):
                        dic_words.append(line)

    return dic_words


def find_anagrams(s, dic):
    """
    :param s: str, the word input by users
    :param dic: list[str], the words highly related to the anagrams
    :return anagrams: list[str], the results for the anagrams
    """
    anagrams = find_anagrams_helper(s, '', [], dic, [])
    return anagrams


def find_anagrams_helper(s, ana, cur_list, dic, used_list):
    """
    :param s:str, the word input by users
    :param ana: empty str, single anagram in the making
    :param cur_list: empty list, storage of the following anagrams
    :param dic: list[str], the words highly related to the anagrams
    :param used_list: empty list, storage of the index of the word input by users
    :param cur_list: list[str], the results for the anagrams
    """
    if len(ana) == len(s) and ana in dic and ana not in cur_list:
        cur_list.append(ana)
    else:
        for i in range(len(s)):
            if i not in used_list:
                used_list.append(i)
                ana += s[i]

                if has_prefix(ana, dic):
                    find_anagrams_helper(s, ana, cur_list, dic, used_list)

                used_list.pop()
                ana = ana[:-1]

    return cur_list


def has_prefix(sub_s, dic):
    """
    :param sub_s:str, the temporary word comprised of the word input by users
    :param dic: list[str], the words highly related to the anagrams
    :return:boolean
    """
    for word in dic:
        if word.startswith(sub_s):
            return True
        else:
            word.startswith(sub_s)
    return word.startswith(sub_s)


if __name__ == '__main__':
    main()
