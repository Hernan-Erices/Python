#AND & (Devuelve true solo si ambas se cumplen (true and true))
Resultado = True & True #Devolver True
Resultado1 = False & True #Devolver False
Resultado2 = True & False #Devolver False
Resultado3 = False & False #Devolver Falso

#OR (Devuelve False solo si ambas no se cumplen (false or false))
Resultado4 = True | True #Devolver True
Resultado5 = False | True #Devolver True
Resultado6 = True | False #Devolver True
Resultado7 = False | False #Devolver Falso


#NOT (Es denegacion si es true es false, si es false es true)
Resultado8 = not True #Devolver Falso
Resultado9 = not False #Devolver True

print(Resultado)