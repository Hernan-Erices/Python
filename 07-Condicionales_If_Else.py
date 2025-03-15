#condicional if (si), codigo a ejecutar en caso de que la condicion se cumple
#else (de lo contrario), codigo a ejecutar en caso de que la condicion no se cumpla


edad = 17

if edad >= 18:
	print("Eres mayor de edad") #se va a ejecutar solo si se cumple la condicion
else:
	print("Eres menor de edad") #si la condicion no se cumplio e ejecutara el else



password = "Hola1234"
password_writed = "Hola123445"

if password == password_writed:
	print("Puedes ingresar")
else:
	print("No puedes pasar")