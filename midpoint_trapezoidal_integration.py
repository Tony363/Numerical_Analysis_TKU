#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan  3 13:53:05 2022

@author: pysolver33
"""

import numpy as np


def midpoint(a,b,n=100):
    return np.abs(a-b)/n

def midpoint_method(n,x0,x1,f=None):
    return np.sum(midpoint(x0,x1,n)*f(np.arange(x0,x1,midpoint(x0,x1,n))))

def trapezoidal_method(n,x0,x1,f=None):
    Y = f(np.arange(x0,x1,midpoint(x0,x1,n)))
    area = 0
    for i,j in zip(range(0,Y.size),range(1,Y.size)):
        area += (Y[i]+Y[j])*midpoint(x0,x1,n) / 2
    return area

if __name__ == "__main__":
    f = np.vectorize(lambda x:x**2 + 2)
    AreaM = midpoint_method(100,0,10,f=f)
    AreaZ = trapezoidal_method(100,0,10,f=f)
    pass