'''
Write a function called most_frequent that takes a string and prints the letters in decreasing order of frequency. 
Find text samples from several different languages and see how letter frequency varies between languages.
Compare your results with the tables at http://en.wikipedia.org/wiki/Letter_frequencies. 
Solution: http://thinkpython2.com/code/most_frequent.py.
'''

def read_file(filename):
    """Returns the contents of a file as a string."""
    return open(filename).read()


def make_histogram(word):
    """Make a map from letters to number of times they appear in word.

    word: string

    Returns: map from letter to frequency
    """
    d = dict()
    for letter in word:
        d[letter] = d.get(letter, 0) + 1
    return d


def most_frequent(word):
    """Sorts the letters in word in range.

    word: string

    Returns: print list of letters
    """

    d = make_histogram(word)
    maxx = max(d.values())

    for i in range (maxx, 0, -1):
        for k in d:
            if d[k] == i:
                print(k, end=', ')

if __name__ == "__main__":
    word = read_file('/home/tin/Documents/my-think-python/words.txt')
    most_frequent(word)
    
