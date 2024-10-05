# ESTA ES LA PRIMERA PARTE DEL ARCHIVO
#Llamamos al archivo
#file=open('my_notes.txt','r')
#print(file)
#lineas=file.readlines()
#print(lineas)
#file.close() # Cerramos el archivo

# Se abre el archivo 'my_notes.txt' en modo escritura
file = open('my_notes.txt', 'w')

# Aquí van las tres líneas de notas personales en el archivo
file.write('Semana de exámenes\n')
file.write('Hay que esrudiar bien\n')
file.write('Tomar en cuenta los horarios de corte de energía eléctrica\n')

# Cierra el archivo después de escribir
file.close()

# Lectura de Archivo de Texto
# Abre el archivo 'my_notes.txt' en lectura
file = open('my_notes.txt', 'r')

# Lee y muestra el contenido del archivo línea por línea
line = file.readline()
while line:
    print(line.strip())  # .strip() elimina los saltos de línea
    line = file.readline()
#print("El archivo tiene {0} caracteres de longitud", format(pos))
# Se cierra el archivo después de leer
file.close()
