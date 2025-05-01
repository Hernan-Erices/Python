archivo = open("texto-python.txt", encoding="utf-8")

#lectura del archivo
# archivo1 = archivo.read() #solo se lee una vez


#leer linea por linea
#lineas = archivo.readlines(0)

#leer una sola linea
linea = archivo.readline()
print(linea)

#cerramos el archivo cuando se deja de usar
archivo.close() #se cierra el archivo, y se debe volver abrir para leerlo de nuevo
