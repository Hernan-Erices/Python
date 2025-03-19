#iteral listas con bucle for, tambien sirve para tuplas
#Iteral sets conjuntos se pueden iteral de la misma manera
lista_animales = ["perro", "gato", "cocodrilo", "loro"]

#Recorriendo la lista animales con el bucle fo
for animal in lista_animales:
	print(animal)

lista_numeros = [1,2,4,5,6]
#Recorriendo la lista de numeros con bucle for y multiplicando cada elemento de la lista
for numero in lista_numeros:
	resultado = numero*3
	print(resultado)

#Recorriendo 2 listas con bucle for usando zip, esto se iteran al mismo tiempo es decir lista1,lista2,lista1,lista2
for numero,animal in zip(lista_animales, lista_numeros):
	print(f"recorriendo lista 1: {numero}")
	print(f"recorriendo lista 2: {animal}")

#For usando range, le damos un rango de numeros a cales debe iterar si pasamos (1,4) iterara 1, 2 y 3
for number in range(5,10):
	print(number)

#Esta no es una forma optima de recorrer una lista, esta forma no sirve para iterar conjuntos sets()
for num in range(len(lista_numeros)):
	print(lista_numeros[num])

#Forma correcta de recorrer una lista con su indice, nos regresa una tupla
for num in enumerate(lista_numeros):
	indice = num[0]
	valor = num[1]
	print(f'el indice es {indice} y el valor es {valor}')

#Ejecutando un bucle y un else al terminar el bucle
for else_numero in lista_numeros:
	print(f'lista de numeros: {else_numero}')
else:
	print("El bucle de la lista termino")


#iterar diccionarios
diccionario = {
	'nombre' : "Alejandro", #clave' : "valor",
	'apellido' : "Arevalo"  #key' : "value"
}

#Recorrer un diccionario con items() para obtener la calve y el valor
for i in diccionario.items():
	key = i[0]
	value = i[1]
	print(f'la calve es {key} y el valor es {value}')


#Iterar lista con bucle for y un if dentro

frutas = ["pera","manzana", "platano", "melon"]

for i in frutas:
	if i == 'pera': 
		continue #aqui omitimos la pera pero continua y si usamos un 'break' cuando llega a la pera el bucle se termina, el else no se ejecuta si se esta usando un 'brake'
	print(f'te comiste la siguiente fruta: {i}')

