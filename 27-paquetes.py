#un paquete es una carpeta con muchos archivos python o modulos
#python identifica un paquete si dentro de la carpeta donde tenemos los modulos tiene el archivo __init_.py

import paquetes.saludar

print(paquetes.saludar.saludar("dentro de un paquete"))
print(type(paquetes))