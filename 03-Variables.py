#Variables es un espacio donde se almacenan datos, datos simples o datos complejos
#En python se recomienda usar snake case para definir el nombre de las variables es decir separar palabras con guin bajo ejemplo nombre_completo
#Esto es una variable ya que es un dato variable, puede cambiar, python lee de arriba para abajo linea por linea.
a = 2 
a = 5
nombre = "Alejandro"
nombre = "Juan"
nombre = "Pedro"
print(a,nombre)

#concatenacion con +
nombre = "Javier"
bievenida = "hola " + nombre + (" como estas?") #esto una concateneacion con +
print (bievenida)

#concateneacion con f string, esta forma de concatenacion transforma todo a texto
pais = "chile"
verdadero = True
bienvenidaa = f"Un gusto {pais} como estas? {verdadero}" #esto es una concateneacion con f string se usa {} y una f antes de iniciar el ""
print(bienvenidaa)

#operadores de pertenecia (in/not in)
print("peru" not in bienvenidaa) #esto es verdadero ya que peru no esta en definido en la variable bienvenidaa
print("chile" in bienvenidaa) #esto igual es verdadero ya que chile si estad presente en la variable de bienvenidaa

 






