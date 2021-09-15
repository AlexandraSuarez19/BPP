from functools import reduce

elementos = [1,2,3,4,5,6,7,8,9,10]

def suma(a,b):
    return a+b

sumatoria = reduce(suma, elementos)


print(sumatoria)