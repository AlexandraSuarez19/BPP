# -*- coding: utf-8 -*-
"""
Created on Wed Sep  8 18:05:02 2021

@author: toshiba
"""

def minimo(lista_numeros):
    minimo = 99999
    for i in lista_numeros:
        if(i < minimo):
            minimo = i
    
    return minimo

def es_primo(n):
    primo = True

    for i in range(2, n-1):
        if(n%i == 0):
            primo = False
    
    return primo

