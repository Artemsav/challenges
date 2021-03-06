#!python3
# Code Challenge 02 - Word Values Part II - a simple game
# http://pybit.es/codechallenge02.html

import itertools
import random
import string
import argparse

from data import DICTIONARY, LETTER_SCORES, POUCH

NUM_LETTERS = 7


def draw_letters():
    """Pick NUM_LETTERS letters randomly. Hint: use stdlib random"""
    return random.choices(POUCH, k=NUM_LETTERS)


def input_word(draw):
    """Ask player for a word and validate against draw.
    Use _validation(word, draw) helper."""
    word = input('Type in your word, use only the letters from draw:').lower()
    if _validation(word, draw) is None:
        return word
    else:
        raise ValueError('Incorrect validation, please print word using only draw-letters')


def _validation(word, draw):
    """Validations: 1) only use letters of draw, 2) valid dictionary word"""

    word_list = list(word)
    function_draw = list(set(x.lower() for x in draw))
    out = []
    if word in DICTIONARY:
        for i in word_list:
            for k in range(len(function_draw)):
                if function_draw[k] == i:
                    out.append(i)
    if len(out) != len(word_list):
        return ValueError

# From challenge 01:
def calc_word_value(word):
    """Calc a given word value based on Scrabble LETTER_SCORES mapping"""
    return sum(LETTER_SCORES.get(char.upper(), 0) for char in str(word))


def _get_permutations_draw(draw):
    """Helper for get_possible_dict_words to get all permutations of draw letters.
    Hint: use itertools.permutations"""
    permutations_draw = {itertools.permutations(draw,i) for i in range(1, (NUM_LETTERS+1))}
    return itertools.chain(*permutations_draw)


# Below 2 functions pass through the same 'draw' argument (smell?).
# Maybe you want to abstract this into a class?
# get_possible_dict_words and _get_permutations_draw would be instance methods.
# 'draw' would be set in the class constructor (__init__).
def get_possible_dict_words(draw):
    possible_words = []
    for get_word in _get_permutations_draw(draw):
        real_word = ''.join(get_word).lower()
        if _validation(real_word, draw) is None:
                possible_words.append(real_word)
    return possible_words


# From challenge 01:
def max_word_value(words):
    """Calc the max value of a collection of words"""
    return max(words, key=calc_word_value)


def main():
    """Main game interface calling the previously defined methods"""
    draw = draw_letters()
    print('Letters drawn: {}'.format(', '.join(draw)))

    word = input_word(draw)
    word_score = calc_word_value(word)
    print('Word chosen: {} (value: {})'.format(word, word_score))

    possible_words = get_possible_dict_words(draw)

    max_word = max_word_value(possible_words)
    max_word_score = calc_word_value(max_word)
    print('Optimal word possible: {} (value: {})'.format(
        max_word, max_word_score))

    game_score = word_score / max_word_score * 100
    print('You scored: {:.1f}'.format(game_score))


if __name__ == "__main__":
    main()
