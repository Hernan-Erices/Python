#todos los modulos son los archivos que tienen un .py
#tenemos 3 tipos de modulos
#Modulos de python estan escritos en c(propios)
#Own modules es decir los modulos propios que fueron creados por nosotros
#Modulos de terceros, son creados por alguien mas

#como ejemplo de modulo vamos a importar el 25-ModulosSaludar.py

#con el 'as' podemos darle un nombre
#import modulo_saludar as saludando
#El dir es para ve las propiedades y metodos de el namespace
#print(dir(saludando))

#saludo = saludando.saludar("Jano2")
#print(saludo)

#Otra forma de importar un modulo donde puedo traer directamente las funciones que usaremos, tambien usamos el 'as' para cambiarle el nombre
from modulo_saludar import saludar as saludar1_con_as, saludar_2 as saludar_con_as

#Mostramos resultados
saludo = saludar1_con_as("Jano2")
print(saludo)

saludo_2 = saludar_con_as("Jano2")
print(saludo_2)

print(type(saludar1_con_as))

