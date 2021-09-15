# -*- coding: utf-8 -*-
"""
Created on Tue Sep  7 13:30:54 2021

@author: toshiba
"""

import pandas as pd
import numpy as np


df = pd.read_csv("C:/Users/toshiba/Documents/Clases_Python/Buenas_Prac/Clase1/finanzas2020.csv", 
                 header = "infer", sep = "\t")


df.head()

df.isnull().values.any()

df.isnull().sum().sum()

first_row = df["Enero"].loc[63]
print(first_row)

"APARTADO 2"
"Compruebe que el fichero existe y que tiene 12 columnas, una para cada mes del año."

try:
    df = pd.read_csv("C:/Users/toshiba/Documents/Clases_Python/Buenas_Prac/Clase1/finanzas2020.csv", 
                 header = "infer", sep = "\t")
    if len(df.columns) == 12:
        print("El archivo se puede abrir y tiene 12 columnas")
except:
    print("No se ha encontrado el archivo")
    
"Para cada mes compruebe que hay contenido"

try: 
    if df.empty:
        print('El fichero no tiene contenido')
except:
    print("El fichero tiene contenido")
else:
    print("Todas las columnas tienen datos")
    
"""Compruebe que todos los datos son correctos. De no haber un dato
correcto, el programa debe saber actuar en consecuencia y continuar
con su ejecución."""

first_row = df["Septiembre"].loc[43]
print(first_row)

df = pd.read_csv("C:/Users/toshiba/Documents/Clases_Python/Buenas_Prac/Clase1/finanzas2020.csv", 
                 header = "infer", sep = "\t")

for i in df.columns:
    try:
        df[[i]] = pd.to_numeric(df[i],errors='coerce')
        df = df.replace(np.nan, 0, regex=True)
        df[[i]] = df[[i]].astype(int)
    except:
        pass
    
print(df.dtypes)

first_row = df["Enero"].loc[63]
print(first_row)

first_row = df["Septiembre"].loc[43]
print(first_row)


"¿Qué mes se ha gastado más?"

df = pd.read_csv("C:/Users/toshiba/Documents/Clases_Python/Buenas_Prac/Clase1/finanzas2020.csv", 
                 header = "infer", sep = "\t")

for i in df.columns:
    try:
        df[[i]] = pd.to_numeric(df[i],errors='coerce')
        df = df.replace(np.nan, 0, regex=True)
        df[[i]] = df[[i]].astype(int)
    except:
        pass

df2 = df

df_gastos = df2[df2 < 0].sum()

print(df_gastos)

df_gastos.min()

# El mes que más se ha gastado es Abril.

"¿Qué mes se ha ahorrado más?"

df = pd.read_csv("C:/Users/toshiba/Documents/Clases_Python/Buenas_Prac/Clase1/finanzas2020.csv", 
                 header = "infer", sep = "\t")

for i in df.columns:
    try:
        df[[i]] = pd.to_numeric(df[i],errors='coerce')
        df = df.replace(np.nan, 0, regex=True)
        df[[i]] = df[[i]].astype(int)
    except:
        pass

df1 = df


df_ahorro = df1.sum()

print(df_ahorro)

df_ahorro.max()

# El mes que más se ha ahorrado es en Enero


"¿Cuál es la media de gastos al año?"

df_gastos.mean()

# La media de gastos al año es de 24732.58

"¿Cuál ha sido el gasto total a lo largo del año? "

df_gastos.sum()

# El total de los gastos es de 296791

"¿Cuáles han sido los ingresos totales a lo largo del año?"

df = pd.read_csv("C:/Users/toshiba/Documents/Clases_Python/Buenas_Prac/Clase1/finanzas2020.csv", 
                 header = "infer", sep = "\t")

for i in df.columns:
    try:
        df[[i]] = pd.to_numeric(df[i],errors='coerce')
        df = df.replace(np.nan, 0, regex=True)
        df[[i]] = df[[i]].astype(int)
    except:
        pass

df3 = df

ingresos = df3.sum()

print(ingresos)

ingresos.sum()

# En total los ingresos se encontrarían en negativo con -15830.

"Realice una gráfica de la evolución de ingresos a lo largo del año"

ingresos.plot()