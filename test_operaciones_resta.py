# -*- coding: utf-8 -*-
"""
Created on Wed Sep  8 17:58:28 2021

@author: toshiba
"""
import pytest
import operaciones_resta

def test_resta():  # Esta operación no recibe parámetro    
    x = 5
    y = 2
    resultado = 3
    assert operaciones_resta.resta(x,y) == resultado
    
