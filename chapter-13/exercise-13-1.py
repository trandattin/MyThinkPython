'''Write a program that reads a file, breaks each line into words, strips whitespace and
punctuation from the words, and converts them to lowercase.
Hint: The string module provides a string named whitespace , which contains space, tab, new-
line, etc., and punctuation which contains the punctuation characters. Let’s see if we can make
Python swear:
>>> import string
>>> string.punctuation
'!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'
Also, you might consider using the string methods strip , replace and translate .
'''
import string


def process_file(filename):
    ''' Read files remove, first line, upper letters, space (get list of word)


    Return: list 
    '''
    res = []
    fin = open(filename)
    for line in fin:
        process_line(line, res)

    return res

def process_line(line, res):
    ''' Remove all of punctuaion, get pure word

    t: list

    Return: List of pure word
    '''
    line = line.replace('-',' ')
    ban_punc = string.punctuation + string.whitespace

    for word in line.split():
        word = word.strip(ban_punc)
        word = word.lower()
        res.append(word)

s = process_file('/home/lark/Documents/my-think-python/country.txt')
print(s)