# -*- coding: utf-8 -*-
"""
Created on Wed Sep  8 18:41:56 2021

@author: toshiba
"""

import unittest
import operaciones_resta
import operaciones
import ejemplofact

# En este caso se tiene que crear una clase.

class PruebasUnitarias(unittest.TestCase):
    def test_resta(self): 
    # Como es una clase tiene que recibir siempre el argumento self.
        x = 5
        y = 2
        resultado = 3
        # Aquí en vez de realizar la función tenemos que utilizar la tabla para
        # saber que se quiere comprobar. 
        self.assertEqual(operaciones_resta.resta(x,y), resultado)
        # Aquí recibe don parámetros. 
        
    def test_factorial(self):
        self.assertEqual(ejemplofact.factorial(5), 120)
            
    def test_es_primo(self):
        self.assertTrue(operaciones.es_primo(7))
        self.assertFalse(operaciones.es_primo(4))

if __name__ == '__main__': 
    unittest.main()
