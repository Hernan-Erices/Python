# 1. Funciones de tipo de dato
print("Ejemplo de type():", type(42))  # Devuelve el tipo de dato del valor 42 (int)
print("Ejemplo de isinstance():", isinstance(42, int))  # Verifica si 42 es un número entero

# 2. Funciones matemáticas
print("Ejemplo de abs():", abs(-7))  # Devuelve el valor absoluto de -7 (7)
print("Ejemplo de round():", round(3.14159, 2))  # Redondea el número pi a 2 decimales (3.14)
print("Ejemplo de max():", max(1, 3, 2, 8, 0))  # Devuelve el valor máximo (8)
print("Ejemplo de min():", min(1, 3, 2, 8, 0))  # Devuelve el valor mínimo (0)
print("Ejemplo de sum():", sum([1, 2, 3, 4]))  # Suma todos los elementos de la lista (10)
print("Ejemplo de pow():", pow(2, 3))  # Calcula 2 elevado a la potencia de 3 (8)

# 3. Funciones para manejo de secuencias
print("Ejemplo de len():", len("Hola"))  # Devuelve la longitud de la cadena "Hola" (4)
print("Ejemplo de range():", list(range(1, 5)))  # Crea una lista con el rango de 1 a 4 ([1, 2, 3, 4])
print("Ejemplo de sorted():", sorted([3, 1, 4, 1, 5, 9]))  # Devuelve la lista ordenada ([1, 1, 3, 4, 5, 9])
print("Ejemplo de reversed():", list(reversed([1, 2, 3])))  # Devuelve el iterable en orden inverso ([3, 2, 1])

# 4. Funciones de entrada/salida
print("Ejemplo de print():", end=" ")
print("¡Hola, Mundo!")  # Imprime "¡Hola, Mundo!" en la consola
# input() espera que el usuario ingrese un valor. Comentamos la siguiente línea para evitar interacciones innecesarias
# name = input("¿Cuál es tu nombre? ")  # Solicita al usuario que ingrese su nombre

# 5. Funciones para trabajar con iteradores
print("Ejemplo de all():", all([True, True, False]))  # Devuelve False porque no todos los valores son True
print("Ejemplo de any():", any([False, False, True]))  # Devuelve True porque al menos un valor es True
print("Ejemplo de enumerate():", list(enumerate(["a", "b", "c"])))  # Devuelve [(0, 'a'), (1, 'b'), (2, 'c')]
print("Ejemplo de zip():", list(zip([1, 2, 3], ["a", "b", "c"])))  # Combina ambos iterables en tuplas [(1, 'a'), (2, 'b'), (3, 'c')]

# 6. Funciones de manejo de excepciones
print("Ejemplo de isinstance():", isinstance(42, int))  # Verifica si 42 es un número entero (True)
print("Ejemplo de repr():", repr("Hola"))  # Devuelve una representación formal de la cadena ("'Hola'")
print("Ejemplo de id():", id("Hola"))  # Devuelve el identificador único del objeto "Hola" (un valor único para ese objeto)

# 7. Funciones para trabajar con objetos de Python
print("Ejemplo de dir():", dir([1, 2, 3]))  # Muestra los métodos y atributos disponibles para una lista
# help() muestra la documentación, pero la dejaremos comentada por razones prácticas
# help(str)  # Muestra la documentación de la clase str
print("Ejemplo de del():", end=" ")
x = 10
print(x)  # Imprime 10
del x  # Elimina la variable x
# print(x)  # Esto generaría un error, ya que x ya no existe.

# 8. Funciones para manipular colecciones
print("Ejemplo de list():", list("Hola"))  # Convierte la cadena en una lista de caracteres: ['H', 'o', 'l', 'a']
print("Ejemplo de set():", set([1, 2, 2, 3, 4]))  # Convierte la lista a un conjunto, eliminando duplicados: {1, 2, 3, 4}
print("Ejemplo de dict():", dict([(1, 'a'), (2, 'b')]))  # Convierte una lista de tuplas en un diccionario: {1: 'a', 2: 'b'}
print("Ejemplo de tuple():", tuple([1, 2, 3]))  # Convierte la lista en una tupla: (1, 2, 3)
