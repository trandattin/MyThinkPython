import sys
import shelve
from anagram_sets import*

def store_anagrams(filename, ad):
    '''Store the anagrams in ad in a shelf

    filename: string file name of shelf
    ad: dictionary that maps string to list of anagrams
    '''
    shelf = shelve.open(filename, 'c')

    for word, word_list in ad.items():
        shelf[word] = word_list

    shelf.close()


def read_anagrams(filename, word):
    '''Look up a word in s shelf 

    filename: string file name of shelf
    word: word to look up
    '''
    shelf = shelve.open(filename)
    sig = signature(word)
    try:
        return shelf[sig]
    except KeyError:
        return []
    

def main(name, command = 'acdlo'):
    if command == 'stored':
        filename = '/home/lark/Documents/my-think-python/anagram.db'
        ad = all_anagrams('/home/lark/Documents/my-think-python/words.txt')
        store_anagrams(filename, ad)
    else:
        print(read_anagrams('/home/lark/Documents/my-think-python/anagram.db', command))

if __name__ == "__main__":
    main(*sys.argv)