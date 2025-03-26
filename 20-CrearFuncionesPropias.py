#Esto es una funcion propia, las funcions propias son las que nosotros creamos y la podemos usar cuantas veces queramos

import math

def area_circulo(radio):
    """Calcula el área de un círculo dado su radio."""
    if radio < 0:
        return "El radio no puede ser negativo."
    area = math.pi * (radio ** 2)
    return area #debemos retornar el valor para poder usar

radio = 5
print(f"El área del círculo con radio {radio} es: {area_circulo(radio)}")



def suma_varios(*numeros):
    """Suma todos los números que se pasen como parámetros."""
    suma = sum(numeros)
    return suma

resultado = suma_varios(3, 5, 10, 2)
print(f"La suma de los números es: {resultado}")

