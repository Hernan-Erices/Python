#diccionarios con dict(), debemos pasarle como parametro calve="valor",
diccionario = dict(nombre="Hernan", apellido="Erices") 

#las listas no pueden ser claves y usamos frozenset para meter conjuntos
diccionario = {frozenset(["Jano","Python"]):"codigo"}

#Creando un diccionaior con fromkeys(), podemos pasar claves sin definir y nos retorna none a cada clave
diccionario = dict.fromkeys(["nombre2","apellido2"])

#Creando diccionario con fromkeys(), cambiando el vlaor por defecto "none" a "no se"
diccionario = dict.fromkeys(["nombre2","apellido2"], "no se")


print(diccionario)