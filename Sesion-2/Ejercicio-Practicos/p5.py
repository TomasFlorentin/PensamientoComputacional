# Crear un programa que le solicite al usuario 5 enteros y muestre por pantalla el promedio de ellos.
# Es muy común usar variables para acumular valores.


print('Ingrese 5 números para calcular el promedio')
num1 = int(input('Num 1: '))
num2 = int(input('Num 2: '))
num3 = int(input('Num 3: '))
num4 = int(input('Num 4: '))
num5 = int(input('Num 5: '))


suma = num1 + num2 + num3 + num4 + num5

print('El promedio de los números es: ', suma/5)