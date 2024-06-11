
#* Crear un programa para abrir un archivo llamado “file.txt” en modo lectura y en caso de que este
#* archivo no exista, mostrar el mensaje “No se pudo encontrar el archivo file.txt”.


try:
    archivo = open('file.txt','r')
    print('Se pudo abrir el archivo!!')
    archivo.close()
except:
    print('No se pudo encontrar el archivo file.txt')
