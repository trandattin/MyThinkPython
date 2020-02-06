'''
Now, letters can be removed from either end, or the middle, but you can’t rearrange any
of the letters. Every time you drop a letter, you wind up with another English word. If
you do that, you’re eventually going to wind up with one letter and that too is going
to be an English word—one that’s found in the dictionary. I want to know what’s the
longest word and how many letters does it have?

I’m going to give you a little modest example: Sprite. Ok? You start off with sprite,
you take a letter off, one from the interior of the word, take the r away, and we’re left
with the word spite, then we take the e off the end, we’re left with spit, we take the s off,
we’re left with pit, it, and I.

Write a program to find all words that can be reduced in this way, and then find the longest one.
'''
def make_word_dict():
    d = dict()
    for line in open('words.txt'):
        word = line.strip().lower()
        d[word] = None
    #add 'a' 'i' ''
    for letter in ['a', 'i', '']:
        d[letter] = letter
    return d

"""memo is a dictionary that maps from each word that is known
to be reducible to a list of its reducible children.  It starts
with the empty string."""
memo = {}
memo[''] = ['']

def is_reducible(word, word_dict):
    '''If word is reducible, returns a list of its reducible children.
    
    Also add entry to the memo dictionary
    A string is reducible if it has at least one child that is
    reducible. The empty string is also reducible.

    children: Return a list of all words that can be formed by removing one letter.
    
    word_dict: dictionary with words as keys

    word: string 

    Return: list of strings
    '''
    if word in memo:
        return memo[word]
    res = []
    for child in children(word, word_dict):
        if is_reducible(child, word_dict):
            res.append(child)
    return res
    
def children(word, word_dict):
    '''Return a list of all words that can be formed by removing one letter.
    
    word: string

    Return: list of 
    '''
    res = list()
    for i in range(len(word)):
        child = word[:i] + word[i+1:]
        if child in word_dict:
            res.append(child)
    return res

def all_reducible(word_dict):
    '''Check all word in word_dict; return a list reducibles one.

    is_reducible: words could and couldn't reducible
    
    word_dict: dictionary with word as keys.
    '''
    res = list()
    for word in word_dict:
        t = is_reducible(word, word_dict)
        if t != []:
            res.append(word)
    return res

def print_trail(word):
    '''Prints the sequence of words that reduces this word to the empty string.
    
    If there is more than one choice, it choice the first.

    word: string
    '''
    if len(word) == 0:
        return
    print(word,)
    t = is_reducible(word, word_dict)
    print_trail(t[0])

def print_longest_words(word_dict):
    #use DSU to sort by word length
    t = list()
    for word in all_reducible(word_dict):
        t.append((len(word), word))
    t.sort(reverse=True)

    #print the 5 longest words
    for length, word in t[0:5]:
        print_trail(word)
        print('\n')

if __name__ == "__main__":
    word_dict = make_word_dict()
    print_longest_words(word_dict)
