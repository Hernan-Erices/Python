cadena1 = "Janooo, erices, arevalo, jano"
cadena2 = "Tengo 23 anios"


minuscula = cadena1.lower() #convierte en minusculas
mayuscula = cadena2.upper() #convierte en mayusculas
primera_letra_mayuscula = cadena1.capitalize() #Convierte la primera letra en mayuscula, pasa todo a lower y despues cambia la primera letra a mayuscula


busqueda_find = cadena1.find("J") #Buscamos una cadena en otra cadena, sino encuentra el valor el resultado sera -1
busqueda_index = cadena1.index("J") #Buscamos una cadena en otra cadena, sino encuentra el valor devuelve una excepcion


es_numerico = cadena1.isnumeric() #Si es numerico, devuelve True sino regresa un False
es_alfanumerico = cadena1.isalpha() #Si es alpha numerico devuelve true, sino regresa un false, si la cadena tiene un espacio no cuenta como alfa numerico, solo cuenta de la a A a la Z


contar_coincidencias = cadena1.count("o") #devuelve la cantidad de veces que coincidencias de una cadena, dentro de otra cadena
contar_caracteres = len(cadena1) #contamos cuantos caracteres tiene una cadena, len es una funcion no un metodo


empieza_con = cadena1.startswith("j") #verificamos si una cadena empieza con otra cadena dada, si es asi devuelve True sino es False
termina_con = cadena1.endswith("o") #verificamos si una cadena termina con otra cadena dada, si es asi devuelve True sino es False

cadena_nueva = cadena1.replace (",",":") #si el valor 1, se encuetra en la cadena original, remplaza el valor 1 de la misma, por el valor 2

cadena_separada = cadena1.split(",") #separar cadena con la cadena que le pasemos, nos devuelve una lista

print(cadena_separada)
