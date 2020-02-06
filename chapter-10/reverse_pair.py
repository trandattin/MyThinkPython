from inlist import *

def reverse_pair(word_list, word):
    rev_word = word[::-1]
    return in_bisect(word_list,rev_word)

if __name__ == "__main__":
    word_list = make_word_list()
    for word in word_list:
        if reverse_pair(word_list, word) and word != word[::-1]:
            print(word, word[::-1])