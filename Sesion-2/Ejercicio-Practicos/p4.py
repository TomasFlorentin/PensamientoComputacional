# Escribir un programa que le pida a un usuario su año de nacimiento y otro año, y le diga qué edad tenía
# el usuario en el año ingresado.

anio_nacimiento = int(input('Ingrese su año de nacimiento: '))

anio = int(input('Ingrese un año para saber que edad tendría en ese año: '))

edad = anio - anio_nacimiento

if edad >= 0:
    print('En el año', anio, ', usted tendría', anio-anio_nacimiento)
else:
    print('Usted no habría nacido para ese año.')

