'''
Two words form a “metathesis pair” if you can transform one into the other by swapping two letters;
for example, “converse” and “conserve”. Write a program that finds all of the metathesis pairs 
in the dictionary. Hint: don’t test all pairs of words, and don’t test all possible swaps
Solution: http://thinkpython2.com/code/metathesis.py. 
Credit: This exercise is inspired by an example at http://puzzlers.org.
'''

def all_anagrams(file_name):
    '''Finds all anagrams in a list of words.

    file_name: string filename of the word list

    Returns: a map from each word to a list of its anagrams.
    '''
    d = dict()
    for line in open(file_name):
        word = line.strip().lower()
        t = signature(word) 
        if t not in d:
            d[t] = [word]
        else:
            d[t].append(word)
    return d


def signature(word):
    ''' Return the signnature of the string, which is a string
    that contains all of the letter in ordered.
    '''
    t = list(word)
    t.sort()
    t = ''.join(t)
    return t


def metathesis_pairs(d):
    """Print all pairs of words that differ by swapping two letters.

    d: map from word to list of anagrams
    """
    print(d)
    for anagrams in d.values():
        for word1 in anagrams:
            for word2 in anagrams:
               if word1 > word2 and word_distance(word1,word2) == 2:
                   print(word1,word2) 


def word_distance(word1,word2):
    """Computes the number of differences between two words.

    word1, word2: strings

    Returns: integer
    """
    count = 0
    for c1,c2 in zip(word1,word2):
        if c1 != c2:
            count += 1
    return count


if __name__ == "__main__":
    d = all_anagrams('words.txt')
    metathesis_pairs(d) 
