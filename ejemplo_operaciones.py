# -*- coding: utf-8 -*-
"""
Created on Mon Sep 13 18:09:18 2021

@author: toshiba
"""

# Lo primero que se debe tener es la documentación inmediata. 
# >>> Cuando lo pongo de esta manera, me cambia el formato. 

class operacionesMatematicas:
    """
    Operaciones matemáticas. Esta clase resuelve una serie de operaciones 
    matemáticas sobre datos de tipo entero.
    
    Atributos: 
        op1: Este es el primer operando que se va a utilizar en el método de 
             operaciones matemáticas.
             En el caso de que el operador que se aplique sea unario, se tendrá
             en cuenta op1 y no op2.
        op2: Este es el segundo operando que se va a utilizar en el método de 
             operaciones matemáticas.
    
    Métodos:
        suma: Suma los operandos op1 y op2.
        resta: Resta los operandos op1 y op2.
        división: Divinde el operando op1 entre el op2. Si op2=0, devuelve 0.
        multiplicación: Realiza el producto entre los operandos op1 y op2.
        es_primo: Determina si un número entero es primo o no primo.
        factorial: Calcula el factorial de op1. 
    
    Ejemplos:
    >>> import operacionesMatematicas
    >>> oM = operacionesMatematicas(5,8)
    >>> resultado_suma = oM.suma()
    >>> resultado_factorial = oM.factorial()
    """

    # Siempre va primero el constructor. __init__
    def __init__(self, op1, op2):
        self.op1 = op1
        self.op2 = op2
        
    def suma(self):
        """
        Método suma: Aplica el algoritmo de la suma sobre los operandos op1 y op2.
        Inputs:
            self.op1: tipo entero
            self.op2: tipo entero
        
        Output:
            res: resultado de sumar op1 y op2
        """
        res = self.op1 + self.op2
        return res
    
    def resta(self):
        """
        Método resta: Aplica el algoritmo de la resta sobre los operandos op1 y op2.
        Inputs:
            self.op1: tipo entero
            self.op2: tipo entero
        
        Output:
            res: resultado de restar op1 y op2        
        """
        res = self.op1 - self.op2
        return res
    
    def producto(self):
        """
        Método producto: Aplica el algoritmo del producto sobre los operandos op1 y op2.
        Inputs:
            self.op1: tipo entero
            self.op2: tipo entero
        
        Output:
            res: resultado de multiplicar op1 y op2                
        """
        res = self.op1 * self.op2
        return res
    
    def division(self):
        """
        Método división: Aplica el algoritmo de la división sobre los operandos op1 y op2.
        Inputs:
            self.op1: tipo entero
            self.op2: tipo entero
        
        Output:
            res: resultado de dividir op1 y op2                
        """
        res = self.op1/self.op2
        return res       
    
    def primo(self):
        """
        Método primo: Determina si el operando op1 es primo o no.
        Inputs:
            self.op1: tipo entero
        
        Output:
            True si self.op1 es primo, False en caso contrario.              
        """
        
        es_primo = True
        for i in (2, self.op1-1):
            if(self.op1%i == 0):
                es_primo = False
                
        return es_primo

    def factorial(self):
        """
        Método para calcular el factorial de un número.
        >>> factorial(5)
        """
        
        assert(n >= 0)
        fct = 1
        for i in range(1, self.op1+1):
            fct *= i
        
        return fct
