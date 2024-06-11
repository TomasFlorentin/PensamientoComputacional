# En un hogar se quieren organizar mejor con las compras, por lo que se quiere guardar en un archivo la
# lista de productos que se necesitan para la próxima vez que la familia vaya al supermercado. Se pide
# hacer un programa que cree un archivo de compras.txt (Ayuda: abrir el archivo en modo w) y le
# pregunte al usuario qué necesita comprar hasta que ingrese una X. Por ejemplo
# > ¿Qué agrego a la lista de compras?
# > Papa
# > ¿Qué agrego a la lista de compras?
# > Pollo
# > ¿Qué agrego a la lista de compras?
# > Fideos
# > ¿Qué agrego a la lista de compras?
# > X
# El archivo tendría que estar de la siguiente forma:
# Papa
# Pollo
# Fideos

archivo = open("compras.txt", "w")

flag = True

while flag:
    opcion = input('¿Qué agrego a la lista de compras?\n').capitalize()
    if opcion != "X":
        archivo.write(opcion+"\n")
    else:
        flag = False



# while opcion != "X":
#     archivo.write(opcion+"\n")
#     opcion = input('¿Qué agrego a la lista de compras?\n').capitalize()
    
