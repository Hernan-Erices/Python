#Inputs strings
nombre = input("Dime tu nombre: ") #Pedimos un dato al usuario, input siempre nos devuelve un string
print(f'El nombre es: {nombre}') #Mostramos el dato almacenado en el input ingresado

#Inputs numericos
numero = input("Ingresa un numero: ") #Pedir un numero al usuario
resultado = int(float(numero) * 4.5) #Convetirmos el valor de la variable numero string a un numero en entero y lo multiplicamos
print(resultado)