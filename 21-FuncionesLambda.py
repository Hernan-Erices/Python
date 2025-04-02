#funcion lambda en Python
# nombre = lamdba x: x + 1

multiplicar_por_dos = lambda x: x * 2
print(multiplicar_por_dos(5))

# Funciones lambda con dos argumentos
# nombre = lambda x, y: x + y
sumar = lambda x, y: x + y
print(sumar(2, 3))

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#creando una funcion comun que diga si es par o no
def es_par(num):
    if num % 2 == 0:
        return True

numeros_pares = list(filter(es_par, numeros))

#usando filter con una funcion comun 
print(numeros_pares)

#usando filter con una funcion lambda
numeros_pares = list(filter(lambda numero: numero % 2 == 1, numeros))
print(numeros_pares)