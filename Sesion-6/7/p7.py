
#* En un cine tienen dos archivos .txt, uno con salas y otro con nombres de películas. Se sabe que en la
#* sala de una fila del archivo se va a transmitir la película de la misma fila del archivo de películas. Se pide
#* leer los dos archivos, y crear un nuevo archivo csv que tenga el nuevo formato sala;pelicula
#* Por ejemplo si se tienen los siguientes archivos:

#* (salas.txt) (peliculas.txt)
#*     D2          Megamente
#*     F1      Rápidos y furiosos
#*     E4          El padrino

#* El nuevo archivo deberá quedar:
#* (funciones.csv)
#* D2;Megamente
#* F1;Rápidos y furiosos
#* E4;El padrino

def crear_archivos():
    #Creo el archivo Salas.txt
    arch_salas = open("salas.txt", "w")
    salas = ['D2','F1','E4']
    for sala in salas:
        arch_salas.write(sala + '\n')
    arch_salas.close()

    # Creo el archivo peliculas.txt
    arch_peliculas = open("peliculas.txt","w")
    peliculas = ['Megamente','Rapidos y furiosos','El padrino']
    for pelicula in peliculas:
        arch_peliculas.write(pelicula + '\n')
    arch_peliculas.close()
crear_archivos()

arch_salas = open("salas.txt", "r")
salas = arch_salas.readlines()
arch_salas.close()
arch_peliculas = open("peliculas.txt", "r")
peliculas = arch_peliculas.readlines()
arch_peliculas.close()

arch_funciones = open("funciones.csv","w") #Creo el archivo para guardar las funciones

if (len(salas)) == (len(peliculas)): #Compruebo si ambas listas tienen igual número de elementos
    for i in range(len(salas)):
        funcion = salas[i].strip('\n') + ';' + peliculas[i]
        arch_funciones.write(funcion)

arch_funciones.close()

# arch_salas = open('salas.txt','r')
# salas = arch_salas.readlines() #Guardo en una lista las salas
# arch_salas.close()
# arch_peliculas = open('peliculas.txt','r')
# peliculas = arch_peliculas.readlines() #Guardo en una lista las peliculas
# arch_peliculas.close()

# funciones = []

# for sala in salas:
#     sala = sala.strip('\n')
#     funciones.append(sala)

# print(funciones)

# arch_salas = open('salas.txt','r') #Abro el archivo de salas
# salas = arch_salas.readlines()
# arch_salas.close()

# arch_peliculas = open('peliculas.txt','r') #Abro el archivo de peliculas
# funciones = []
# arch_salas = open('salas.txt','r')
# for i in range(len(salas)):
#     sala = arch_salas.readline()
#     pelicula = arch_peliculas.readline()
    
#     funciones.append(sala)
#     funciones.append(pelicula)

# for funcion in funciones:
#     funcion = funcion.strip('\n')
#     print(funcion)
# print(funciones)


