# -*- coding: utf-8 -*-
"""
Created on Wed Sep  8 17:49:10 2021

@author: toshiba
"""



def factorial(n):
    fct = 1
    for i in range(1, n+1):
        fct *= i
    
    return fct