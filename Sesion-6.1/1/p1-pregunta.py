# Se tiene un archivo con la pregunta “¿Cómo estás hoy?” llamado pregunta.txt. 
# Se pide leerlo y mostrar la pregunta por pantalla para luego pedirle al usuario que 
# ingrese una respuesta. Después, guardar la respuesta dada por el usuario en el archivo.

# Por ejemplo,se tiene el archivo pregunta.txt que originalmente tiene:
# ¿Cómo estás hoy?

# Y el usuario de la respuesta: “¡Bien, porque me comí una hamburguesa!”

# Entonces el archivo debería quedar de la forma:
# ¿Cómo estás hoy?
# ¡Bien, porque me comí una hamburguesa!

def defineArchivo():
    archivo = open("pregunta.txt", "w")
    archivo.write("¿Como estás hoy?\n")
    archivo.close()

defineArchivo()

# Leo el alchivo
archivo = open("pregunta.txt", "r+")
pregunta = archivo.read() # Guardo la pregunto en una variable
print(pregunta)

respuesta = input('')
archivo.write(respuesta) # Escribo la respuesta en el archivo
archivo.close()

