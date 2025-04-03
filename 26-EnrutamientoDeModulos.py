#Aqui estamos ingresando al directorio (/funciones)
import funciones.saludar

#Mostramos resultados, debemos ingresar dentro de la carpeta
saludo = funciones.saludar.saludar("Enrutamiento")
print(saludo)

saludo_2 = funciones.saludar.saludar_2("Hola")
print(saludo_2)

#otra forma de importar un modulo
import sys
sys.path.append("C:\\Users\\Jano\\Documents\\Python\\funciones")

import saludar as modulo_saludo

print(modulo_saludo.saludar("saludo con sys"))