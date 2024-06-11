
#* Una profesora tiene una lista de diccionarios para guardar las notas que sacaron sus alumnos en el
#* último parcial que tomó. Cada uno de esos diccionarios tiene el nombre del alumno, su apellido, su dni
#* y la nota que sacó.

#* a. Hacer una función que reciba este diccionario, y guarde las notas en un archivo csv, llamados
#* notas.csv

#* b. Tiempo después de guardar las notas, la profesora quiso saber la cantidad de alumnos que
#* aprobaron. Hacer una función que lea el archivo creado en el ejercicio anterior, y devolver la
#* cantidad de alumnos aprobados (su nota es mayor a 4).

def cargar_notas_alumnos(diccionario): #A
    archivo = open("notas.csv","w") # Creo el archivo notas.csv
    for alumno in diccionario:
        alu = ';'.join(str(alumno['nota'])) + '\n' #Paso a string la nota de los alumnos para agregarle salto de linea
        archivo.write(alu)
        
    archivo.close()

def alumnos_aprobados():
    aprobados = 0

    archivo = open("notas.csv","r")
    notas = archivo.readlines() #Leo las notas de los archivos
    archivo.close()

    for nota in notas:
        nota = int(nota.strip('\n')) #Paso a entero el numero
        if nota > 4:
            aprobados += 1
    print (f'La cantidad de alumnos aprobados son: {aprobados}')


diccionario_alumnos = [
    {
        "nombre": "Juan",
        "apellido": "Perez",
        "dni": 12345,
        "nota": 7
    },
    {
        "nombre": "Candela",
        "apellido": "Pereyra",
        "dni": 23456,
        "nota": 6
    },
    {
        "nombre": "Agustin",
        "apellido": "Morimoto",
        "dni": 34567,
        "nota": 2
    },
    {
        "nombre": "Elias",
        "apellido": "Rodriguez",
        "dni": 45678,
        "nota": 3
    },
    {
        "nombre": "Mateo",
        "apellido": "Galeano",
        "dni": 56789,
        "nota": 9
    }
]

cargar_notas_alumnos(diccionario_alumnos)
alumnos_aprobados()