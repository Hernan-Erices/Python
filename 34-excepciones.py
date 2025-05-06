# creando funcion que suma numeros
def sumar_dos():
    #iniciando un bucle while
    while True:
        #pidiendo numero
        a = input("Numbero 1: ")
        b = input("Numbero 1: ")
        #intentando covertirlos a enteros y sumarlos
        try:
            resultado = int(a) + int(b)
        #si lanzo una excepcion, pedirle que reingrese los datos
        except Exception as e:
            print("te pedi un numero")
            print(f"ERROR: {type(e).__name__}")
        #si todo salio bine terminamos el bucle
        else:
            break
        finally:
            print("finally se ejecuta siempre, rara vez se usa")
    #mostrando resultado
    return resultado

print(sumar_dos())