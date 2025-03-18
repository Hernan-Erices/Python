lista = list(["Jano", "Erices"]) #Creando una lista con list()
lista_numerica = list([9,4,3,345,3, True, False]) #Creando una lista con list()

resultado_len = len(lista) # len devuelva la cantidad de elementos en la lista

lista.append("AJIOOOO") #agrega elementos a la lista con append

lista.insert(2,"Alejandro") #agregar un elementos a la lista en un indice especifico

lista.extend([7,"janito", "janitroo"]) #agregar varios elementos a la lista de forma de una lista

lista.pop(1) #Elimina un elemento de una lista indicando el indice, si se le agrega el indice -1 se elimina el ultimo elemento

lista.remove("Jano") #Elimina un elemento de la lista por el valor

lista_numerica.sort(reverse=True) #Ordena la lista de menor a mayor, si se usa el parametro reverse=True lo ordena en reversa

lista_numerica.reverse() #invierte los elementos de la lista

elemento_buscado = lista.index(6) #verifica si un elemento se encuentra en la lista

lista_numerica.clear() #Elimina todos los elementos de la lista

print(elemento_buscado)