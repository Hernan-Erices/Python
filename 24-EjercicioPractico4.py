#creando una funcion que muestre la serie fibonacci entre 0 y el numero dado

def fibonacci(num):
    a,b = 0,1
    fibonacci_list = [0]
    for i in range(num):
        if b > num: return fibonacci_list
        else: 
            fibonacci_list.append(b)
            a,b = b, a+b

resultado = fibonacci(100)
print(resultado)

#Buscar una mejor manera de hacerlo