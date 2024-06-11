# Se tiene un archivo csv que contiene información sobre el stock de una librería. Se guarda por cada
# línea, el nombre del producto, el código, el precio por unidad y el stock actual, es decir:
# nombre;código;precio;stock
# Un posible ejemplo de este archivo es el siguiente:
# lapiceras;34512;50;120
# cuadernos;41611;500;130
# sacapuntas;62812;30;210
# …

# Se pide:
# a. Leer el archivo y mostrarlo por pantalla con el siguiente formato:
# Nombre producto: lapiceras
# Código producto: 34512
# Precio por unidad: 50
# Stock: 120
# Nombre producto: cuadernos
# Código producto: 41611
# Precio por unidad: 500
# Stock: 130
# …

archivo = open("libreria.csv","r")
productos_crudo = archivo.readlines()
archivo.close()

def transformar(producto):
    producto = producto.strip("\n") # Le quito el \n a cada elemento
    producto = producto.split(";") # Separo a los elementos por ;
    return producto

productos = list(map(transformar, productos_crudo))

for producto in productos:
    [nombre, codigo, precio, stock] = producto
    print(f'Nombre producto: {nombre}\nCódigo producto: {codigo}\nPrecio por unidad: {precio}\nStock: {stock}\n')


# b. Hacer una función que reciba un diccionario que describa una línea del archivo y lo agregue, es
# decir que si se recibe un diccionario del tipo
# {
# “nombre”: “hojas A4”,
# “código”: 35662,
# “precio”: 600,
# “stock”: 45
# }

def agregar_producto(diccionario):
    nombre = diccionario["nombre"]
    codigo = str(diccionario["codigo"])
    precio = str(diccionario["precio"])
    stock = str(diccionario["stock"])
    producto = [nombre, codigo, precio, stock]
    print(producto)
    archivo = open("libreria.csv","a")
    ele = ';'.join(producto)+'\n' #Guardo en un string los elementos de producto separado por ;
    archivo.write(ele)
    archivo.close()


diccionario_producto = {
    "nombre": "hojas A4",
    "codigo": 35662,
    "precio": 600,
    "stock": 45
}

agregar_producto(diccionario_producto)