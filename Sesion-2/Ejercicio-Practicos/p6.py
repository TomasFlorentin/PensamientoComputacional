# Crear una función que reciba un número y muestre el anterior y el siguiente.

num = int(input('Ingrese un número: '))

def anterior_siguiente(num):
    num_anterior = num - 1
    num_siguiente = num + 1
    print('El número anterior de', num, 'es', num_anterior, 'y el siguiente es', num_siguiente)


anterior_siguiente(num)