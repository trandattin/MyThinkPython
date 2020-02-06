# -*- coding: utf-8 -*-
"""
Created on Tue Jan  7 14:25:05 2020

@author: Tran Tin
Finished
"""
def rotate_letter(letter, n):
    """Rotates a letter by n places.  Does not change other chars.

    letter: single-letter string
    n: int

    Returns: single-letter string
    """
    if letter.isupper():
        start = ord('A')
    elif letter.islower():
        start = ord('a')
    else:
        return letter

    c = ord(letter) - start
    i = (n + c) % 26 + start 
    return chr(i)
            
def rotate_word(word, step):
    res = ''
    for letter in word:
        res += rotate_letter(letter, step)
    return res
         

print(rotate_word('The quick brown fox jumps over 13 lazy dogs.',39))
    
