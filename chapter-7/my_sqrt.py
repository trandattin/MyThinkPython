"""
Exercise 7.1.
Copy the loop from Section 7.5 and encapsulate it in a function called mysqrt
that takes a as a parameter, chooses a reasonable value of x, and returns an
estimate of the square root of a.
To test it, write a function named test_square_root that prints a table like this:
a   mysqrt(a)      math.sqrt(a)   diff
-   ---------      ------------   ----
1.0 1.0            1.0            0.0
2.0 1.41421356237  1.41421356237  2.22044604925e-16
3.0 1.73205080757  1.73205080757  0.0
4.0 2.0            2.0            0.0
5.0 2.2360679775   2.2360679775   0.0
6.0 2.44948974278  2.44948974278  0.0
7.0 2.64575131106  2.64575131106  0.0
8.0 2.82842712475  2.82842712475  4.4408920985e-16
9.0 3.0            3.0            0.0
The first column is a number, a;
the second column is the square root of a computed with mysqrt;
the third column is the square root computed by math.sqrt;
the fourth column is the absolute value of the difference between the two estimates.
"""

import math


def my_sqrt(a):
    x = 3 * a / 2
    epsilon = 0.000001
    while True:
        estimated_root = (x + a / x) / 2
        # Make the result more accuracy
        if abs(x - estimated_root) < epsilon:
            return estimated_root
            break
        x = estimated_root


def pattern(a, my_sqrt, math_sqrt, diff):
    # first column
    print(a, ' ' * (3 - len(str(a))), end=' ')
    # second column
    print(my_sqrt, ' ' * (15 - len(str(my_sqrt))), end=' ')
    # forth column
    print(math_sqrt, ' ' * (15 - len(str(math_sqrt))), end=' ')
    # fifth column
    print(diff)


def line():
    # first line
    pattern('a', 'mysqrt(a)', 'math.sqrt(a)', 'diff')
    # second line
    pattern('-', '-' * 9, '-' * 11, '-' * 4)
    # the rest
    for value_a in range(1, 10):
        # value of a
        a = float(value_a)
        # my sqrt
        b = round((my_sqrt(float(value_a))), 13)
        # math.sqrt
        c = round((math.sqrt(value_a)), 13)
        # diff
        d = math.sqrt(value_a) - my_sqrt(value_a)
        pattern(a, b, c, d)


line()
