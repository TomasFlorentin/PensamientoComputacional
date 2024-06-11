# Escribir código que dado dos enteros, determine si la suma de ambos da menos que 100. Si la suma de
# ambos es menor a 100, calcular cuánto falta para llegar a 100 y mostrar por pantalla un mensaje con
# ese valor. Si la suma es mayor a 100, mostrar un mensaje diciendo “Llega a 100”.
# Extra: ¿Cómo harían para que el programa quede generalizado para cualquier límite, a elección del
# usuario, y no solo para 100?.

limite = 100

num1 = int(input('Ingrese un entero: '))
num2 = int(input('Ingrese otro entero: '))

if (num1 + num2) < 100:
    falta = 100 - (num1 + num2)
    print(f'Falta {falta} para llegar a 100.')
else:
    print('Llega a 100')
