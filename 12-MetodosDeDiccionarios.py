diccionario = {
	"Nombre":'Hernan',
	"Apellido":'Erices',
	"Edad": 23
}

claves = diccionario.keys() #keys devuelve las claves, tambien nos sirve para iterar

valor_de_nombre = diccionario.get("Nombre") #get() Nos devuelve el valor de una clave, cuando no encuentra el valor nos regresa un 'none' que no tiene valor y el programa continua con su flujo

diccionario.pop("Edad") #pop() elimina un elemento del diccionario

diccionario_iterable = diccionario.items()  #Obtener elemento dict_items iterable

limpiar_diccionario = diccionario.clear() #clear() elimina todo el dicionario y nos regresa 'none'

print(diccionario_iterable)
