'''
Write a function named uses_only that takes a word and a string of letters, and
that returns True if the word contains only letters in the list. Can you make a sentence using only
the letters ❝ acefhlo”? Other than “Hoe alfalfa”?
by: Lark
Last edited: 01/08/2020
Finished
'''

def uses_only(word, available):
    for char in word:
        if char not in available:
            return False
    return True
