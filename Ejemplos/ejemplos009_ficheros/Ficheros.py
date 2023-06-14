# Manejo de Ficheros.docx

print('\n*** 1. ABRIR UN FICHERO ***')

# Lectura
# Si el fichero no existe: error
ficheroLectura = open('miFichero.txt', 'r')

# Escritura
# Si el fichero no existe: se crea
ficheroEscritura = open('miFichero.txt', 'w')

# Agregar contenido al final del mismo
# Si el fichero no existe: se crea
ficheroAgregar = open('miFichero.txt', 'a')

# Modo binario
# Se puede agregar a cualquiera de los modos anteriores
# Modo de lectura binaria
fichero = open('miFichero.bin', 'rb')
# Modo de escritura binaria
fichero = open('miFichero.bin', 'wb')
# Modo de agregar binario
fichero = open('miFichero.bin', 'ab')



print('\n*** 2. LEER UN FICHERO ***')

# Lee todo el contenido
contenido = fichero.read()
# Lee una linea
linea = fichero.readline()
# Lee todas las lineas
lineas = fichero.readlines()



print('\n*** 3. ESCRIBIR EN UN FICHERO ***')

# Escribe una línea
fichero.write('Hola, mundo!\n')
# Escribe varias líneas
fichero.writelines(['Línea 1\n', 'Línea 2\n', 'Línea 3\n'])



print('\n*** 4. CERRAR UN FICHERO ***')

with open('nombre_fichero.txt', 'r') as fichero:
	contenido = fichero.read()
	# Realiza operaciones con el fichero

# El fichero se cerrara automaticamente al salir del bloque "with"