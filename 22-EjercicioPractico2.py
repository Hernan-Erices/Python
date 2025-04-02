#1 alumno es profesor
#2 alumno es asistente

#(A) Pedir la edad de los companeros que vinieron hoy a clases y ordenar
#los datos de menos a mayor

#(B) El mayor es el profesor y el menor es el asistente:
#Quien es quien?

#pedir nombre y la edad de los companeros que vinieron hoy a clase
def obtener_companeros(cantidad_companeros):
    companeros = []
    for i in range(cantidad_companeros):
        nombre = input("Nombre: ")
        edad = int(input("Edad: "))
        companeros.append((nombre, edad))
    companeros.sort(key=lambda x: x[1])
    asistente = companeros[0][0]
    profesor = companeros[-1][0]
    return asistente, profesor

asistente, profesor = obtener_companeros(3)
print(f"El asistente es {asistente} y el profesor es {profesor}")
