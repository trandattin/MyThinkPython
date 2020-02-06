def make_word_list():
    fin = open('words.txt')
    word_list = []
    for line in fin:
        word = line.strip()
        word_list.append(word)
    return word_list

def in_bisect(word_list,word):
    if len(word_list) == 0:
        return False

    i = len(word_list) // 2
    if word_list[i] == word:
        return True
    
    if word_list[i] > word:
        return in_bisect(word_list[:i], word)

    else:
        return in_bisect(word_list[i+1:], word)

if __name__ == "__main__":
    word_list = make_word_list()

    for word in ['aa']:
        print(word, 'in list', in_bisect(word_list, word))