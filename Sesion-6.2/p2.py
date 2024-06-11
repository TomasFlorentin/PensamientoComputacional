
#* Crear una función, utilizando el punto anterior, que le pida al usuario un número entero. Utilizarla para
#* calcular el producto entre dos números enteros ingresados

def num_entero():
    es_entero = False
    while not es_entero:
        try:
            num = input('Ingrese un número entero: ')
            num = int(num) #Intento pasarlo a Entero
            es_entero = True #Si puedo convertirlo a int, entonces cambio la bandera
        except:
            print('Ups el número ingresado no es un entero.')
    return num


print('Ingrese dos números enteros para hacer su producto.\n')
num1 = num_entero()
print('Ingrese el segundo valor.')
num2 = num_entero()

print(f'El producto entre {num1}x{num2} es: {num1*num2}')