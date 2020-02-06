'''Exercise 13.8. Markov analysis:

1. Write a program to read a text from a file and perform Markov analysis. The result should be
a dictionary that maps from prefixes to a collection of possible suffixes. The collection might
be a list, tuple, or dictionary; it is up to you to make an appropriate choice. You can test your
program with prefix length two, but you should write the program in a way that makes it easy
to try other lengths.

2. Add a function to the previous program to generate random text based on the Markov analysis.
Here is an example from Emma with prefix length 2:
He was very clever, be it sweetness or be angry, ashamed or only amused, at such
a stroke. She had never thought of Hannah till you were never meant for me?" "I
cannot make speeches, Emma:" he soon cut it all himself.
For this example, I left the punctuation attached to the words. The result is almost syntacti-
cally correct, but not quite. Semantically, it almost makes sense, but not quite.
What happens if you increase the prefix length? Does the random text make more sense?

3. Once your program is working, you might want to try a mash-up: if you combine text from
two or more books, the random text you generate will blend the vocabulary and phrases from
the sources in interesting ways.
'''

import random
import string
import sys

suffix_map = {}
prefix = ()


def process_file(file_name, order=2):
    """ Reads a file and performs Markov analysus

    file_name: string
    order: integer number of words in the prefix

    Returns: map from prefix to list of possible suffixes.
    """
    fin = open(file_name)
    for line in fin:
        for word in line.split():
            process_word(word, order)            


def process_word(word, order=2):
    """ Processes each word.

    word: string
    order: integer

    During the first few iterations, all we do is store up the words'
    after that we start adding entries to the dictionary
    """
    global prefix #because prefix is imutable

    if len(prefix) < order:
        prefix += (word,)
        return
    
    try:
        #if there is have entry for this prefix, add word as value
        suffix_map[prefix].append(word)
    except KeyError:
        #if there is no entry for this prefix, make one
        suffix_map[prefix] = [word]
    
    prefix = shift(prefix, word)


def shift(prefix, word):
    """Forms a new tuple by removing the head and adding word to the tail.

    prefix: tuple of strings
    word: string

    Returns: tuple of string
    """
    return prefix[1:] + (word,)
        

def random_text(n=100):
    """Generates random words from the analyzed text.

    Starts with a random prefix from the dictionary.

    n: number of words to generate
    """
    # choose a random prefix (not weighted by frequency)
    start = random.choice(list(suffix_map.keys()))
    
    for i in range(n):
        suffixes = suffix_map.get(start, None)
        if suffixes == None:
            # if the start isn't in map, we got to the end of the
            # original text, so we have to strat again.
            print()
            print('*********************')
            print()
            random_text(n-i)
            return

        # choose a random suffix
        word = random.choice(suffixes)
        print(word, end=' ')
        start = shift(start, word)


def main(name, file_name='/home/lark/Documents/my-think-python/half_a_bee.txt', order=2, n=100, *arg):
    try:
        order = int(order)
        n = int(n)
    except:
        print ('Usage: randomtext.py filename [# of words] [prefix length]')
    else:
        process_file(file_name,order)
        print(suffix_map)
        random_text(n)


if __name__ == "__main__":
    main(*sys.argv)