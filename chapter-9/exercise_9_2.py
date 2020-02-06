''' In 1939 Ernest Vincent Wright published a 50,000 word novel called Gadsby that
does not contain the letter “e”. Since “e” is the most common letter in English, that’s not easy to
do.
In fact, it is difficult to construct a solitary thought without using that most common symbol. It is
slow going at first, but with caution and hours of training you can gradually gain facility.
All right, I’ll stop now.
Write a function called has_no_e that returns True if the given word doesn’t have the letter “e” in
it.
Write a program that reads words.txt and prints only the words that have no “e”. Compute the
percentage of words in the list that have no “e”.
by: Lark
Last edited: 01/08/2019
Finished
'''


def has_no_e(word):
    for char in word:
        if char == 'e' or char == 'E':
            return False
    return True

def main():
    fin = open('words.txt')

    total_words = 0
    words_without_e = 0
    percent_without_e = 0

    for line in fin:
        word = line.strip()
        if has_no_e(word):
            print(word)
            words_without_e += 1
        total_words += 1
    
    percent_without_e = words_without_e / total_words
    print(percent_without_e)

main()