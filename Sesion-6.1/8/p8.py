
#* Santi le fue mostrando colores a sus amigos y cada amigo le fue diciendo si le gusta o no. Guardó cada
#* respuesta en un .csv de la siguiente manera: 
#* nombre;color;le gusta, 
#* pero se dió cuenta que no es una forma muy práctica de guardarlo, así que lo quiere cambiar. 

#* Hacer un programa que lea el archivo y lo transforme en un archivo .txt. 
#* Es decir que si se tiene un archivo csv de la siguiente forma:

#*      .csv                            .txt
#*  Agus;verde;si            A Agus sí le gusta el verde
#*  Tomi;violeta;no          A Tomi no le gusta el violeta
#*  Manu;marrón;no           A Manu no le gusta el marrón


archivo = open("colores.csv","r")
colores = archivo.readlines() #Guardo las variables en color
archivo.close()

persona = [] #Creo una lista para guardar las frases
for color in colores:
    color = color.strip('\n') #Le stripo el salto de linea
    color = color.split(';') #Separo por ;
    if color[2] == 'no':
        persona.append(f'A {color[0]} no le gusta el {color[1]}')
    elif color[2] == 'si':
        persona.append(f'A {color[0]} si le gusta el {color[1]}')

archivo = open("colores.txt","w") #Creo el archivo
for i in range(len(persona)):
    archivo.write(persona[i]+'\n')
archivo.close()
