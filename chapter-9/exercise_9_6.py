'''
Write a function called is_abecedarian that returns True if the letters in a word
appear in alphabetical order (double letters are ok). How many abecedarian words are there?
by: Lark
Last edited: 01/08/2019
'''

def is_abecedarian1(word):
    # for loops
    previous = word[0]
    for c in word:
        if c < previous:
            return False
    return True

def is_abecedarian2(word):
    # while loops
    i = 0
    while i < len(word)-1:
        if word[i] > word[i+1]:
            return False
        i += 1 
    return True

def is_abecedarian3(word):
    #recursion
    if len(word) <= 1:
        return True
    if word[0] > word[1]:
        return False
    return is_abecedarian3(word[1:])

