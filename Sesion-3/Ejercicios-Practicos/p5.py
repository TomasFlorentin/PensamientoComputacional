# Crear el programa al que sea imposible ganarle en el juego de “Piedra, papel o tijera”. Cada elemento va
# a ser representado con una letra: R para piedra, P para papel y T para tijera.
# a. Hacer una función que le haga al usuario ingresar alguna de esas letras, e imprima por pantalla
# la jugada para ganarle. 
# Por ejemplo:
# > ¡Juguemos! Ingresá piedra ( R), papel (P) o tijera (T)
# > P
# > Tijera. ¡Te gané!
# ATENCIÓN: Observar cómo se usa una frase inicial para darle a entender al usuario lo que tiene
# que hacer (en este caso ingresar alguna de las tres letras).
# b. Mostrar por pantalla el mensaje “NO vale” cuando el usuario ingresa una letra no válida
# (distinta de R, P o T).

opcion = input('¡Juguemos! Ingresá piedra (R), papel (P) o tijera (T):\n')

invalido = True

while invalido:
    if opcion in 'RPT':
        invalido = False
        break
    print('NO vale')
    opcion = input('¡Juguemos! Ingresá piedra (R), papel (P) o tijera (T):\n')

if opcion == 'R':
    opcion_compu = 'Papel'
elif opcion == 'P':
    opcion_compu = 'Tijera'
elif opcion == 'T':
    opcion_compu = 'Piedra'


print(f'{opcion_compu}. ¡Te gané!')