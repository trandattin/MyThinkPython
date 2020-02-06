'''
Write a function named uses_all that takes a word and a string of required letters,
and that returns True if the word uses all the required letters at least once. How many words are
there that use all the vowels aeiou? How about aeiouy?
by: Lark
Last edited: 01/08/2020
Finished
'''

from exercise_9_4 import uses_only

def uses_all(word, string_of_letter):
    return uses_only(string_of_letter, word)
