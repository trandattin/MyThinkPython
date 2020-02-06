def make_keys():
    d = dict()
    fin = open('words.txt')
    for line in fin:
        word = line.strip()
        d[word] = d.get(word, 0) 
    return d

print(make_keys())  
