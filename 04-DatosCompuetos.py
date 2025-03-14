#Listas es un tipo de matriz que es un conjunto de datos
lista = ["Alejandro", "Chile", True, 1.71] #las listas usan corchetes []
lista[1] = "Peru"
print(lista[1]) #aqui unicamente estoy extrayendo el elemento 1 que viene siendo el 0 el 2do elemento es el 1 y asi sucesivamente

#Tuplas, a diferencia de las listas, las tuplas no se puede modificar
tupla = ("Alejandro", "Chile", True, 1.71) #las tupleas usan parentesis ()
print(tupla[1])

#Conjunto (set), No se puede modificar, no se puede acceder al indice de los elementos [0][1] etc, no se puede repetir datos, No muestra los elementos ordenados
conjunto = {"Alejandro", "Chile", True, 1.71, 1.71} #los conjuntos usan llaves {}
print(conjunto)

#Diccionarios (dict), Le podemos dar un nombre a cada indice con 'clave' : "valor"
diccionario = {
	'nombre' : "Alejandro", #clave' : "valor",
	'apellido' : "Arevalo"  #key' : "value"
}
print(diccionario['apellido'])