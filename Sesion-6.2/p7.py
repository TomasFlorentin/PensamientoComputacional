
#* Para jugar al truco con un único mazo de cartas españolas, el número de jugadores puede ser: dos,
#* cuatro o seis. Crear una función que pida al usuario informar el número de jugadores, considerando
#* que este puede ingresar:
#* ● un valor no válido, por ejemplo, una palabra.
#* ● un valor menor a 2, en en cuyo caso, mostrar el mensaje "Debe haber al menos 2 jugadores."
#* ● un valor mayor a 6, en cuyo caso, mostrar el mensaje "Se puede jugar con un máximo de 6
#* jugadores.".
#* ● un valor impar, como 3 y 5, en cuyo caso, mostrar el mensaje "Debe haber un número par de
#* jugadores.".
#* ● un valor válido, en cuyo caso, mostrarlo

print('Juego: TRUCO!!')
es_entero = False

while not es_entero:
    try:
        jugadores = input('Ingrese el número de jugadores!: ')
        jugadores = int(jugadores)
        if jugadores%2 == 1:
            print('Debe haber un número par de jugadores.')
        elif jugadores < 2:
            print('Debe haber al menos 2 jugadores.')
        elif jugadores > 6:
            print('Se puede jugar con un máximo de 6 jugadores.')
        else:
            print('Que comience el juego!!')
            es_entero = True
    except:
        print('Debe ingresar un número entero.')