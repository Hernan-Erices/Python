#Ejercicio 1
#a) diferencia en procentaje entre el curso actual y:
# - El mas rapido de otros cursos
# - El mas lento de otros cursos
# - El promedio de los cursos
print("EJERCICIO 1 ")
print("---------------------- ")
print("---------------------- ")
#Promedio de duracion
otros_cursos_min = 2.5
otros_cursos_max = 7
otros_cursos_promedio = 4
dalto_curso = 1.5

#Diferncias de duracion
print("A ------------------------------------------------")
diferencia_con_min = 100 - (dalto_curso / otros_cursos_min * 100)
print(f'El curso de dalto dura un {diferencia_con_min}% menos que el mas rapido')

diferencia_con_max = 100 - (dalto_curso *1000 // otros_cursos_max / 10)
#diferencia_con_max_int = int(diferencia_con_max)
print(f'El curso de dalto dura un {diferencia_con_max}% menos que el mas lento')

diferencia_con_promedio = 100 - (dalto_curso / otros_cursos_promedio * 100)
print(f'El curso de dalto dura un {diferencia_con_promedio}% menos que el promedio')

#b) Que porcentaje de material inservible que se reduce en:
# - El promedio de los cursos
# - El curso actual (Este curso)

#Duracion de crudos, crudo es el video sin editar
crudo_promedio = 5
crudo_dalto = 3.5

#calcular el porcentaje de tiempo vacio removido
tiempo_vacio_promedio = 100 - otros_cursos_promedio * 1000 // crudo_promedio / 10
tiempo_vacio_dalto = 100 - dalto_curso * 1000 // crudo_dalto / 10

print("B------------------------------------------------")
print(f'Un curso promedio elimina un {tiempo_vacio_promedio}% de tiempo vacio')
print(f'Este curso elimina un {tiempo_vacio_dalto}% de tiempo vacio')



#c) Ver 10 horas de este curso a cuantas de otros cursos equivale?
print("C ------------------------------------------------")
print(f'Ver 10 horas de este curso equivalen a ver {otros_cursos_promedio * 100 // dalto_curso / 10} horas de otros cursos')
print(f'Ver 10 horas de otros curso equivalen a ver {dalto_curso * 100 // otros_cursos_promedio / 10} horas de este curso')


print("EJERCICIO 2")
print("---------------------- ")
print("---------------------- ")

# a) Pedirle al usuario que cualquier texto real y:
# - Calcular cuanto tardaria en decir esa frase
# - Cuantas palabras dijo?
# b) Si tarda mas de un minuto:
# - Decirle:"Para tampoco te pedi un testamento"
# c) Dalto habla un 30% mas rapido: cuanto tardaria el en decirlo?
frase = input("Di una frase y te calculo cuanto tardarias en decirlo:")
palabras_separadas = frase.split(" ")
cantidad_de_palabras = len(palabras_separadas)
print(f'Dijiste {cantidad_de_palabras} palabras, y tardarias {cantidad_de_palabras/2} segundos en decirlo')
print(f'Yo lo diria en {cantidad_de_palabras * 100 // 2 * 1.3 / 100} segundos')

if cantidad_de_palabras > 120:
	print("Tampoco te dije que escribieras la biblia")