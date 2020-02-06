'''
Write a function named avoids that takes a word and a string of forbidden letters,
and that returns True if the word doesn’t use any of the forbidden letters.
Write a program that prompts the user to enter a string of forbidden letters and then prints the
number of words that don’t contain any of them. Can you find a combination of 5 forbidden letters
that excludes the smallest number of words?
by: Lark
Last edited: 01/08/2019
Finished
'''

def avoids (word, avoid_list):
    for char in word:
        if char in avoid_list:
            return False
    return True
    