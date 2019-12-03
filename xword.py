#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Crossword Solver Program"""

__author__ = "SmileySlays"

import re
import itertools

# YOUR HELPER FUNCTION GOES HERE


def crossword_solver(test_word, dictionary_words):
    solutions = []
    test_word_list = list(itertools.chain(test_word))
    # print(test_word_list)
    for index, word in enumerate(test_word_list):
        if word == " ":
            test_word_list[index] = "\w"
    re_pattern = "".join(test_word_list)
    # print(re_pattern)
    for word in dictionary_words:
        if len(word) == len(test_word_list):
            match = re.findall(r'{0}'.format(re_pattern), word)
            if len(match) > 0:
                solutions.append(match[0])
    if len(solutions) == 0:
        print("\nPlease only insert valid word characters with appropriate spaces!\n")
    else:
        return '\n'.join(solutions) + '\n'


def main():
    with open('dictionary.txt') as f:
        words = f.read().split()

    test_word = input(
        'Please enter a word to solve.\nUse spaces to signify unknown letters: ').lower()

    # YOUR ADDITIONAL CODE HERE
    print("\nSolutions:\n", crossword_solver(test_word, words))


if __name__ == '__main__':
    main()
