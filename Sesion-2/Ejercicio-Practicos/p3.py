# Crear un programa que le solicite al usuario un entero y determine si es par, mostrando por pantalla un
# mensaje que indique el resultado.
# Para determinar si un número es par o impar, se puede determinar con el uso del operador %, les
# dejamos a ustedes el cómo.

num1 = int(input('Ingrese un número para determinar si es par o impar: '))

if num1%2 == 0:
    print('El número es Par')
else:
    print('El número es impar')