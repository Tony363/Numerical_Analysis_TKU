#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 12 12:59:17 2021

@author: pysolver33
"""

import numpy as np
import pandas as pd

def f(x):
    return x**3+x-1
    return x**3+x+1
    return x**10-1
    return (x**2)-4

# Implementing Bisection Method
def bisection(x0,x1,e):
    step = 1
    print('\n\n*** BISECTION METHOD IMPLEMENTATION ***')
    condition = True
    while condition:
        x2 = (x0 + x1)/2
        print('Iteration-%d, x2 = %0.6f and f(x2) = %0.6f' % (step, x2, f(x2)))

        if f(x0) * f(x2) < 0:
            x1 = x2
        else:
            x0 = x2
        
        step = step + 1
        condition = abs(f(x2)) > e

    print('\nRequired Root is : %0.8f' % x2)

if __name__ == '__main__':
    # Input Section
    x0 = np.float128(input('First Guess: '))
    x1 = np.float128(input('Second Guess: '))
    e = np.float128(input('Tolerable Error: '))
    
    # Converting input to float
    # x0 = float(x0)
    # x1 = float(x1)
    # e = float(e)
    
    #Note: You can combine above two section like this
    # x0 = float(input('First Guess: '))
    # x1 = float(input('Second Guess: '))
    # e = float(input('Tolerable Error: '))
    
    
    # Checking Correctness of initial guess values and bisecting
    if f(x0) * f(x1) > 0.0:
        print('Given guess values do not bracket the root.')
        print('Try Again with different guess values.')
    else:
        bisection(x0,x1,e)
   
    
