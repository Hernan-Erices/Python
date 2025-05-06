#creando mi propia excepcion personalizada
class MiExcepcion(Exception):
    def __init__(self,err):
        print(f"este es el error: {err}")

#lanzando mi propia excepcion 
#raise MiExcepcion ("tonto")

#manejandola
try:
    raise MiExcepcion ("tonto")
except:
    print("cometiste un error")