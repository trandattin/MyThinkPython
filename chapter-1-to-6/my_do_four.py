#do_four.py (finished)
# Last edited: 12/31/2019
# by:tran_dat_tin


def do_twice(f, value):
    f(value)
    f(value)


def print_spam(spam):
    print(spam)


def do_four(f, value):
    do_twice(f, value)
    do_twice(f, value)


do_four(print_spam, 'spam')
