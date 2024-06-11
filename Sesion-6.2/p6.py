
#* Para jugar al chinchón con un único mazo de cartas españolas, el número de jugadores puede ser: dos,
#* tres o cuatro. Crear una función que pida al usuario informar el número de jugadores, considerando
#* que este puede ingresar:
#* ● un valor no válido, por ejemplo, una palabra. 
#* ● un valor menor a 2, en en cuyo caso, mostrar el mensaje "Debe haber al menos 2 jugadores."
#* ● un valor mayor a 4, en cuyo caso, mostrar el mensaje "Se puede jugar con un máximo de 4
#* jugadores."
#* ● un valor válido, en cuyo caso, mostrarlo


print('Juego: CHINCHÓN!!')
es_entero = False

while not es_entero:
    try:
        jugadores = input('Ingrese el número de jugadores!: ')
        jugadores = int(jugadores)
        if jugadores < 2:
            print('Debe haber al menos 2 jugadores.')
        elif jugadores > 4:
            print('Se puede jugar con un máximo de 4 jugadores')
        else:
            print('Pueden empezar con el juego!')
            es_entero = True
    except:
        print('Debe ingresar un número entero.')