# -*- coding: utf-8 -*-
"""
Created on Sun Jan  5 14:31:58 2020

@author: Tin Tran
"""

def eval_loop():
    while True:
        value = input('>>> ')
        
        if value == 'done':
            break
        else:
            print(eval(value))
                
eval_loop()

