# usamos 'a' para agregar texto a un archivo existente, no sobreescribe el texto y lo agrega al final del archivo en cada ejecucion

with open("texto-python.txt", 'a', encoding="utf-8") as archivo:

    #uisando un bucle for para agregar varias lineas al archivo
    for i in range(5):
        archivo.write(f"linea {i+1} agregada\n")

    #desafio escribir el mismo codigo en una sola linea
    