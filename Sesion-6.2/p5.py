
#* Crear una función cuyos parámetros sean una lista y un índice de posición para mostrar el valor de la
#* lista en esa ubicación.

#* a. ¿Qué ocurre si ingreso un índice que se encuentra fuera del rango?

#* b. Si el valor del índice ingresado se encuentra dentro del rango, mostrar el valor. En caso
#* contrario, mostrar un mensaje apropiado para dicho error

def mostrar_valor(lista, index):
    try:
        print(lista[index])
    except IndexError:
        print('El valor del indice indicado, se encuentra fuera de rango.')

en_rango = False

frutas = ['Pera','Manzana','Naranja','Frutilla']

while not en_rango:
    try:
        posicion = int(input('Ingrese el indice que desea mostrar: '))
        mostrar_valor(frutas,posicion)
        en_rango = True
    except:
        pass


