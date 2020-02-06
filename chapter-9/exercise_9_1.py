''' Write a program that reads words.text and prints only the words with more than 20
characters (not counting whitespace).
by: Lark
Last edited: 01/08/2019
Finished
'''

fin = open('words.txt')
for line in fin:
    word = line.strip()
    if len(word) > 20:
        print(word)