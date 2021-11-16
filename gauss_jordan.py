#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 16 13:21:24 2021

@author: pysolver33
"""


# Importing NumPy Library
import numpy as np
import sys

def input_coefficients(n,matrix):
    # Reading augmented matrix coefficients
    print('Enter Augmented Matrix Coefficients:')
    for i in range(n):
        for j in range(n+1):
            matrix[i][j] = float(input( 'm['+str(i)+']['+ str(j)+']='))
    return matrix
            
def gauss_jordan(n,matrix):
    # Applying Gauss Jordan Elimination
    for i in range(n):
        if matrix[i][i] == 0.0:
            sys.exit('Divide by zero detected!')
            
        for j in range(n):
            if i != j:
                ratio = matrix[j][i]/matrix[i][i]
    
                for k in range(n+1):
                    matrix[j][k] = matrix[j][k] - ratio * matrix[i][k]
    return matrix

def solution(x,n,matrix):
# Obtaining Solution
    for i in range(n):
        x[i] = matrix[i][n]/matrix[i][i]
    return x

if __name__ == '__main__':
    # Reading number of unknowns
    n = int(input('Enter number of unknowns: '))
    
    # Making numpy array of n x n+1 size and initializing 
    # to zero for storing augmented matrix
    matrix = np.zeros((n,n+1))
    
    # Making numpy array of n size and initializing 
    # to zero for storing solution vector
    x = np.zeros(n)

    matrix = input_coefficients(n,matrix)
    matrix = gauss_jordan(n,matrix)
    x = solution(x,n,matrix)

    # Displaying solution
    print('\nRequired solution is: ')
    for i in range(n):
        print('X%d = %0.2f' %(i,x[i]), end = '\t')