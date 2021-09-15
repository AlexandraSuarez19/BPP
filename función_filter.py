elementos = [1,2,3,4,5,6,7,8]

def es_par(n):
    return n%2==0

pares = list(filter(es_par, elementos))

print(pares)