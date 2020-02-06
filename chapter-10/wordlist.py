def built_list1():
    fin = open('words.txt')
    t = []
    for line in fin:
        word = line.strip()
        t.append(word)
    return t

def built_list2():
    fin = open('words.txt')
    t = []
    for line in fin:
        word = line.strip()
        t += [word]
    return t

print(built_list1())