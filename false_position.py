#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 19 12:19:50 2021

@author: pysolver33
"""
import numpy as np
import pandas as pd

def fp(xu,xl):
    return xu - ((f(xu)*(xl-xu))/(f(xl)-f(xu)))

def f(x):
    return x**2 - 4

if __name__ == '__main__':
    xl,xu = 0,3
    tolerance = 0.0000001
    matrix = []
    for _ in range(20):
        xr = fp(xu,xl)
        solution = (abs(f(xr)-f(xu)) < tolerance) or (abs(f(xr)-f(xl)) < tolerance)
        matrix.append([xu,xl,xr,f(xl),f(xu),f(xr),solution])
        xu = xr if np.sign(f(xu)*f(xr)) == 1 else xu 
        xl = xr if np.sign(f(xl)*f(xr)) == 1 else xl
        print([xl,xu,xr,f(xl),f(xu),f(xr)])
        # print(f(xl),f(xr))
    
    pd.DataFrame(
        matrix,
        columns=[
            'xu','xl','xr',
            'f(xl)','f(xu)','f(xr)','solution'
            ]
        ).to_csv("excels/false_position.csv")
    
