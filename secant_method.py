#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 26 12:38:58 2021

@author: pysolver33
"""
import numpy as np
import pandas as pd

def f(x):
    return np.float128(x**3+x-1)
    return np.float128(x**3+x+1)
    return np.float128(x**10-1)
    return np.float128((x**2)-4)

def secant(x0,x1,e,N):
    print('\n\n*** SECANT METHOD IMPLEMENTATION ***')
    step = 1
    condition = True
    while condition:
        if f(x0) == f(x1):
            print('Divide by zero error!')
            break
        
        x2 = x0 - (x1-x0)*f(x0)/( f(x1) - f(x0) ) 
        print('Iteration-%d, x2 = %0.6f and f(x2) = %0.6f' % (step, x2, f(x2)))
        x0 = x1
        x1 = x2
        step = step + 1
        
        if step > N:
            print('Not Convergent!')
            break
        
        condition = abs(f(x2)) > e
    print('\n Required root is: %0.8f' % x2)

if __name__ == "__main__":
    # Input Section
    x0 = np.float128(input('Enter First Guess: '))
    x1 = np.float128(input('Enter Second Guess: '))
    e = np.float128(input('Tolerable Error: '))
    N = np.int64(input('Maximum Step: '))
    
    # Converting x0 and e to float
    # x0 = float(x0)
    # x1 = float(x1)
    # e = float(e)
    
    # Converting N to integer
    # N = int(N)
    
    
    #Note: You can combine above three section like this
    # x0 = float(input('Enter First Guess: '))
    # x1 = float(input('Enter Second Guess: '))
    # e = float(input('Tolerable Error: '))
    # N = int(input('Maximum Step: '))
    
    # Starting Secant Method
    secant(x0,x1,e,N)