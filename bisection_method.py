#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 12 12:59:17 2021

@author: pysolver33
"""

import numpy as np
import pandas as pd

def f(x):
    return (x**2)-4

def step_function(fxl,fxr,prev,m):
    if np.sign(fxl*fxr)<0:
        return prev
    return m

def midpoint(x0,x1):
    return (x0+x1)/2

def mse(xl,xu):
    return (xl-xu)**2

if __name__ == '__main__':
    xl = 0
    row = []
    for i in range(10):
        if i == 0:
            xu = xl + 3
        xi = midpoint(xl,xu)
        fxl = f(xl)
        fxu = f(xu)
        fxr = f(xi)
        test = mse(xl,xu)
        print(f"xl:{xl}")
        print(f"xu:{xu}")
        print(f"fxl:{fxl}")
        print(f"fxu:{fxu}")
        print(f"fxr:{fxr}")
        print()
        row.append([xl,xu,xi,fxl,fxu,fxr,test])
        xu = step_function(fxu,fxr,xu,xi)
        xl = step_function(fxl,fxr,xl,xi)
    result = pd.DataFrame(row,columns=['xl','xu','xi','fxl','fxu','fxr','mse'])
    result.to_csv("excels/bisection.csv")
   
    
