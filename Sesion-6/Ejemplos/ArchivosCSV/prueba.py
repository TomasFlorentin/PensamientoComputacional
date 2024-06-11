#Genera Planilla Ingegrada de Datos
completo = open('datosCompletos.csv','w') #Creo el archivo
b = [] #Creo lista vacía

datos = open('datos1.csv','r')
a = datos.readlines()
datos.close()

for i in range(len(a)):
    a[i] = a[i].strip('\n') #Quito los saltos de linea
    a[i] = a[i].split(';') #Separo los elementos cuando haya una ;
    a[i][3] = int(a[i][3]) #Paso a entero los elementos en esta posición

b+= a #Agrego la lista A a B

for elemento in b:
    elemento[3] = str(elemento[3])
    print(elemento)
    ele = ';'.join(elemento) + '\n'
    print(ele)
    completo.write(ele)
completo.close()