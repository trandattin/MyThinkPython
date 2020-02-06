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
import random


def process_file(filename, skip_header):
    '''Make a histogram that contains the words from a file.
    
    filename: string

    skip_header: boolean, whether to skip the Gutenberg header

    Return: map from each word to the number of times it appears
    '''
    hist = {}
    fin = open(filename)
    

    if skip_header:
        skip_gutenberg_header(fin)

    for line in fin:
        if line.startswith('*** END OF THIS'):
            break
        process_line(line, hist)

    return hist


def skip_gutenberg_header(fin):
    """Read from fin until it finds the line that ends the header.

    fin: open file objet
    """
    for line in fin:
        if line.startswith('*** START OF THIS'):
            break

def process_line(line, hist):
    ''' Remove space, punctuation and adds the pure words in the line to the histogram.
    
    Modifies hist.

    line: string

    hist: histogram (map from word to frequency)
    '''
    # replace hyphens with spaces before splitting
    line = line.replace('-',' ')
    ban_punc = string.punctuation + string.whitespace + '“”.,'

    for word in line.split():
        # remove punction and convery to lowercase
        word = word.strip(ban_punc)
        word = word.lower()

        #update the histogram
        hist[word] = hist.get(word, 0) + 1


def total_word(hist):
    """Returns the total of the frequencies in a histogram."""
    return sum(hist.values())

def total_diff_word(hist):
    """Return the total of different words in a histogram."""
    return len(hist.keys())

def most_common(hist):
    """Make a list of the key-value pairs from a histogram and sorts them in descending order by frequency.
    
    hist: histogram (map from word to frequency)

    Return: list of word
    """
    res = []

    for k,v in hist.items():
        res.append((v, k))

    res.sort(reverse=False)
    return res

def print_most_common(hist, num):
    """Prints the most commons words in a histogram and their frequencies.

    hist: histogram (map from word to frequency)

    num: number of words to print
    """
    t = most_common(hist)
    
    for freq, word in t[num:]:
        print(word, freq, sep='\t')

def subtract(d1,d2):
    """Returns a dictionary with all keys that appear in d1 but not d2.

    d1, d2: dictionary
    """
    return set(d1) - set(d2)

def random_word(h):
    """Choose a random word from a histogram.
    
    the probability of each word is proportional to its frequency.
    """
    t = []
    for word, freg in h.items():
        t.extend([word]*freg)

    return random.choice(t)

if __name__ == "__main__":
    hist = process_file('/home/tin/Documents/my-think-python/country.txt', skip_header = True)
    t = total_word(hist)
    print(t)

