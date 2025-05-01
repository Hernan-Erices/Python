#abrimos un archivo de texto y escribimos en él usando el modo 'w' (write),
#Si no encuentra el archivo, lo crea, y si lo encuentra, lo sobreescribe
with open("texto-python.txt", 'w', encoding="utf-8") as archivo:
    #archivo.write("Hola mundo\n")

    archivo.writelines(["Hola mundo\n", "Hola mundo 2\n", "Hola mundo 3\n"]) #escribimos varias lineas a la vez, y no sobreescribe el texto
    archivo.writelines(["no sobre escribe\n", "no sobre escribe el texto\n", "no sobre escribe\n"])