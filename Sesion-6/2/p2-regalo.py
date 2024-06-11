# En un archivo llamado regalo.txt se tiene la lista de las personas que quieren participar en el regalo de
# cumpleaños de Sol (en cada línea está el nombre de una persona). El encargado de organizar el regalo
# es Ale, y quiere saber más información antes de ir a comprarle algo a Sol.

# a. Mostrar por pantalla los nombres de las personas que quieren participar en el regalo.

# b. Se sabe que quieren poner 1000 pesos por persona por regalo. Hacer una función que devuelva
# cuánto dinero tiene Ale para hacerle el regalo a Sol. Es decir si se tiene un archivo de esta forma:
# Agus
# Manu
# Santi
# Lorena
# Maria
# La función tiene que devolver 5000

# c. Tomi sabe que si participa Santi, también participa Tomi. Se pide que si Santi está en el archivo
# de los nombres, se agregue también a Tomi.


def crearArchivo(): # Creo el archivo con los nombres de los participantes
    archivo = open("regalo.txt","w")
    personas = ['Agus', 'Manu', 'Santi', 'Lorena', 'Maria'] #Lista con los nombres
    for i in personas: # Recorro y escribo los nombres en el archivo
        archivo.write(i + "\n")
    archivo.close()

def dineroTotal(nombres): # Función que recibe una lista de parámetro
    dinero = 0
    for persona in nombres: # Recorro la lista
        dinero += 1000
        print(persona.strip("\n"))
        if (persona.strip('\n') == "Santi"): # Verifico si Santi está en la lista
            dinero += 1000
            print("Tomi")
    return dinero # Devuelvo la suma de dinero

crearArchivo()

# Abro y leo el archivo
archivo = open("regalo.txt", "r+")

nombres = archivo.readlines() # Leo el archivo y lo guardo en una lista
print("Las personas que van a participar del regalo son:")
# for persona in nombres: # Muestro los nombres de las personas
#     print(persona.strip("\n")) # Elimino los espacios al principio y al final del string

dinero = dineroTotal(nombres)

print(f"El dinero con el que cuenta Ale es {dinero}")

archivo.close()