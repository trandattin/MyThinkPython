'''Exercise 13.5. Write a function named choose_from_hist that takes a histogram as defined in
Section 11.2 and returns a random value from the histogram, chosen with probability in proportion
to frequency. For example, for this histogram:

>>> t = ['a', 'a', 'b']
>>> hist = histogram(t)
>>> hist
{'a': 2, 'b': 1}
your function should return 'a' with probability 2/3 and 'b' with probability 1/3.
'''

import random

def histogram(s):
    '''Process a string to map from letters to number
    of times they appear in the string(s).
    
    s: string of letter

    Return: map from word to its frequency
    '''
    d = dict()
    for letter in s:
        d[letter] = d.get(letter,0) + 1
    return d
    
def choice_my_hist(h):
    '''Process a map to list 
   
    d: map from letter to its frequency

    Print random a letter 
    '''
    d = histogram(h)
    
    res = []
    for k,v in d.items():
        res.extend(k*v)

    random_key = random.choice(res)
    print('Random ',random_key)

choice_my_hist(['a','a','b','c'])
