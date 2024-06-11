
#* El kiosko de la facultad quiere automatizar un letrero que tome datos de un programa y le cobre al
#* estudiante.
#* Se tienen dos diccionarios, uno con un código y el producto, y otro con el código y el precio de cada
#* producto.
#* Ejemplo:

#* opciones = {                      valores = {
#*   1:"hamburguesas",                 1:1000,
#*   2:"milanesas",                    2:1500,
#*   3:"gaseosa",                      3:500,
#*   4:"alfajor",                      4:300,
#*   5:"papas fritas",                 5:600,
#*   6:"agua"                          6:350
#* }                                 }

#* Se quiere hacer un programa que muestre la información de la siguiente forma en la pantalla:
#* 1: hamburguesas -> 1000
#* 2: milanesas -> 1500
#* 3: gaseosa -> 500
#* 4: alfajor -> 300
#* 5: papas fritas -> 600
#* 6: agua -> 350

#* Y le pida al usuario una opción y una cantidad. Luego, debe imprimir el total a pagar.
#* Se debe considerar que el usuario podría ingresar 
#* una opción que no está en el diccionario, 
#* ingresar una opción que no sea un número. 
#* El usuario debe en esos casos imprimir un mensaje de error que sea
#* descriptivo y volver a pedirle al usuario que ingrese una opción

opciones = {
    1:"hamburguesas",
    2:"milanesas",
    3:"gaseosa",
    4:"alfajor",
    5:"papas fritas",
    6:"agua"
}

valores = {
    1:1000,
    2:1500,
    3:500,
    4:300,
    5:600,
    6:350
}

def menu(opciones, menu):
    print('MENU:')
    if len(opciones) == len(menu):
        for i in range(len(opciones)):
            print(f'{i+1}: {opciones[i+1]} -> {valores[i+1]}')

menu(opciones,valores)

def opcion_valida():
    es_entero = False
    while not es_entero:
        try:
            opcion = input('Ingrese una opcion: ')
            opcion = int(opcion)
            es_entero = True
        except:
            print('No es un número')
    
    return opcion

en_rango = False

while not en_rango:
    try:
        opcion = opcion_valida()
        print(f'La opción seleccinada es: {opciones[opcion]}')
        print('Ingrese la cantidad que desea:')
        cantidad = opcion_valida()
        total = cantidad * valores[opcion]
        en_rango = True
    except KeyError:
        print('El valor ingresado no se encuentra en el rango.')

print(f'El total a pagar es: {total}')


