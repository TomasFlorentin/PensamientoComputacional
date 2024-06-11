
#* Se quiere hacer un programa para pedirle al usuario que ingrese un número entero, y en caso de que el
#* valor ingresado no sea un número entero, mostrarle un mensaje apropiado.
#* a. Realizarlo utilizando isnumeric(). ¿Qué limitaciones encuentra? La limitación es que si hay un error salta el programa en el medio
#* b. Realizarlo utilizando try/ except

es_entero = False

# while not es_entero:
#     num = input('Ingrese un número entero: ')
#     if num.isnumeric():
#         es_entero = True
#     else:
#         print('El número ingresado no es un entero, intente de nuevo.')

# print('El número ingresado es entero y es ' + num)


while not es_entero:
    try:
        num = input('Ingrese un número entero: ')
        numero = int(num)
        es_entero = True
    except:
        print('Ups, no ingresaste un entero, intente de nuevo.')
    
print('El número ingresado fue un entero y es ' + num)