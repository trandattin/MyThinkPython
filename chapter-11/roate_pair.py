def rotate_letter(letter, n):
    """Rotates a letter by n places.  Does not change other chars.

    letter: single-letter string
    n: int

    Returns: single-letter string
    """
    if letter.isupper():
        start = ord('A')
    elif letter.islower():
        start = ord('a')
    else:
        return letter

    c = ord(letter) - start
    i = (n + c) % 26 + start 
    return chr(i)

def rotate_word(word, step):
    res = ''
    for letter in word:
        res += rotate_letter(letter, step)
    return res

def make_word_dict():
    d = {}
    fin = open('words.txt')
    for line in fin:
        word = line.strip().lower()
        d[word] = word
    return d

def rotated_pairs(word,word_dict):
    for i in range(1,14):
        rotated = rotate_word(word, i)
        if rotated in word_dict:
            print(word, i, rotated)


for word in make_word_dict():
    rotated_pairs(word, make_word_dict())