#Desempaqutado de variables
datos_tupla = ("Hernan", "Erices", 23) #Esto es una tupla
datos_lista = ["Jano","Erices", 23] #Esto es una lista
datos_set= {"Jano","Erices", 23} #Esto es un conjunto

nombre,apellido,edad = datos_lista #Esto es el desempaquetado de la variable
nombre,apellido,edad = datos_tupla #Esto es el desempaquetado de la variable
nombre,apellido,edad = datos_set #Esto es el desempaquetado de la variable
print(nombre)

#Tuplas
tupla = tuple(["dato1", "dato2"]) #Otra forma de crear una tupla con la funcion tuple()
tupla = "dato1","dato2", #Esto igual es una tupla sin parentesis, si queremos unicamente un dato seria "dato1", con la coma para diferenciarlo con un string
print(tupla)


#Set o Conjuntos
#Los set no se pueden modificar

conjunto = set(["dato1", "dato2"])

#Poniendo un conjunto dentro de otro conjunto con frozenset

conjunto1 = frozenset(["dato1", "dato2"]) #esto crea un conjunto inmutable
conjunto2 = {conjunto1, "dato3"}

print(conjunto2)

#Teoria de conjuntos
#Verificar si es un subconjunto
conjunto3 = {1,3,5,7}
conjunto4 = {1,3,7}
resultado = conjunto4.issubset(conjunto3) #con issubset podemos saber si es un subconjunto del conjunto
resultado_alternativo = conjunto4 <= conjunto3 #Funciona igual que la funcion issubset, aca tiene que ser mayor o igual que

#Verificar si es un superconjunto
resultado_si_es_un_super_conjunto = conjunto4.issuperset(conjunto3) #aca verificamos si es un superconjunto con issuperset
resultado_si_es_un_super_conjunto = conjunto4 > conjunto3 #funciona igual que el issuperset aca tiene que ser mayor que


#Verificar si hay algun numero en comun
resultado_valor_en_comun = conjunto4.isdisjoint(conjunto3) #isdisjoint solo devolvera TRUE si los conjuntos que se estan comparando no tiene nigun valor igual

print(resultado_valor_en_comun)
