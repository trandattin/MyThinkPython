# -*- coding: utf-8 -*-
"""
Created on Sun Jan  5 19:28:16 2020

@author: HP
"""

prefixes = 'JKLMNOPQ'
suffix = 'ack'

for letter in prefixes:
    if letter == 'O' or letter == 'Q':
        print (letter + 'u' + suffix)
    else:
        print(letter + suffix)