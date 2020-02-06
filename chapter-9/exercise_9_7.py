"""This module contains code from
Think Python by Allen B. Downey
http://thinkpython.com

Copyright 2012 Allen B. Downey
License: GNU GPLv3 http://www.gnu.org/licenses/gpl.html

http://www.cartalk.com/content/seeing-double
"""

def is_triple_double (word):
    i = 0
    count = 0
    while i < len(word)-1:
        if word[i] == word[i+1]:
            count += 1
            if count == 3:
                return True
            i += 2
        else: 
            i += 1
    return False

def find_word ():
    fin = open('words.txt')
    for line in fin:
        word = line.strip()
        if is_triple_double(word):
            print(word)

find_word()
            
        

