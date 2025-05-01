

with open("texto-python.txt", encoding="utf-8") as archivo: #abriendo el archivo con with open
    print(archivo.read()) #se abre el archivo y se lee todo de una vez

#No es necesario cerrar el archivo, ya que se cierra automaticamente al salir del bloque with