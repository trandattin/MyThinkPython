# -*- coding: utf-8 -*-
"""
Created on Sun Jan  5 15:45:59 2020

@author: Tran Tin

Exercise 7.3.

The mathematician Srinivasa Ramanujan found an infinite series that can be used to
generate a numerical approximation of 1/pi.
https://en.wikipedia.org/wiki/Pi#Rapidly_convergent_series
Write a function called estimate_pi that uses this formula to compute and return
an estimate of pi. It should use a while loop to compute terms of the summation
until the last term is smaller than 1e-15 (which is Python notation for 10**-15).
You can check the result by compar
ing it to math.pi.
Solution: http://thinkpython2.com/code/pi.py

"""

import math

def factorial(value):
    if value == 0:
        return 1
    else:
        return factorial(value - 1) * value

def estimate_pi():
    k = 0
    total = 0
    factor = 2 * math.sqrt(2) / 9801
    while True:
        num = factorial(4 * k) * (1103 + 26390 * k)
        den = (factorial(k) ** 4 * 396 ** (4 * k))
        result = factor * num / den
        total += result
        
        if abs(result) < 1e-15:
            break
        k += 1
        
    return 1 / total
        
print(estimate_pi())
    
    
