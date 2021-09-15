elementos = [2,3,4,5,7,17]

def elevar_cuadrado(n):
    return n**2

resultado = list(map(elevar_cuadrado, elementos))

print(resultado)