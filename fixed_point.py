#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov  9 12:32:03 2021

@author: pysolver33
"""

# Fixed Point Iteration Method
# Importing math to use sqrt function
import math

def f(x):
    return x**3 + x**2 -1

# Re-writing f(x)=0 to x = g(x)
def g(x):
    return 1/math.sqrt(1+x)

# Implementing Fixed Point Iteration Method
def fixedPointIteration(x0, e, N):
    print('\n\n*** FIXED POINT ITERATION ***')
    step = 1
    flag = 1
    condition = True
    while condition:
        x1 = g(x0)
        print('Iteration-%d, x1 = %0.6f and f(x1) = %0.6f' % (step, x1, f(x1)))
        x0 = x1

        step = step + 1
        
        if step > N:
            flag=0
            break
        
        condition = abs(f(x1)) > e

    if flag==1:
        print('\nRequired root is: %0.8f' % x1)
    else:
        print('\nNot Convergent.')

if __name__ == '__main__': 
    x0 = float(input('Enter Guess: '))
    e = float(input('Tolerable Error: '))
    N = int(input('Maximum Step: '))
    
    # Starting Newton Raphson Method
    fixedPointIteration(x0,e,N)
