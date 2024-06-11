# Se tiene un archivo con el siguiente texto:
# Paco Peco, chico rico,
# insultaba como un loco
# a su tío Federico;
# y éste dijo: Poco a poco,
# Paco Peco, poco pico. Me han dicho que has dicho un dicho
# que han dicho que he dicho yo,
# el que lo ha dicho, mintió,
# y en caso que hubiese dicho
# ese dicho que tú has dicho
# que han dicho que he dicho yo,
# dicho y redicho quedó.
# y estaría muy bien dicho,
# siempre que yo hubiera dicho
# ese dicho que tú has dicho
# que han dicho que he dicho yo.

# Se pide hacer un programa que pida dos palabras: una que se quiera reemplazar y la palabra por la que
# se quiera reemplazar, cambie el texto y lo guarde en el archivo otra vez. Por ejemplo, si la función
# recibe “poco” y “mucho”, reemplaza “poco” por “mucho” todas las veces que aparezca en el texto

palabra_reemplazar = input('¿Qué palabra queres reemplazar?\n')

palabra_nueva = input('¿Por qué palabra la querés reemplazar?\n')

# Abro el archivo para leer
archivo_lectura = open('archivo.txt', 'r')
texto = archivo_lectura.readlines() # Guardo las oraciones en una lista
archivo_lectura.close()


# Abro el archivo para escribir
archivo_escritura = open('archivo.txt', 'w')
for linea in texto: # Recorro linea por linea
    archivo_escritura.write(linea.replace(palabra_reemplazar,palabra_nueva)) # Uso el método replace para modificar strings
archivo_escritura.close()

