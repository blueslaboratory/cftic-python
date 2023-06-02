print('\n *** EJERCICIO 2 ***')
nombre = input('Nombre completo: ')



print('Nombre en minusculas: ')
print(nombre.lower())
print('Nombre en mayusculas: ')
print(nombre.upper())
print('Nombre con iniciales en mayusculas: ')
print(nombre.title())

# En una linea
print
print(nombre.lower(), nombre.upper(), nombre.title(), sep='\n')



print('\n*** EJERCICIO 6 ***')

asignaturas = ['Matemáticas', 'Física', 'Química', 'Historia', 'Lengua']
asignaturasSuspensas = asignaturas.copy()
notas = []
i = 0

for i in range(len(asignaturas)):
	nota = round(float(input('Nota ' +asignaturas[i] +': ')), 2)
	if(nota<=5.0):
		notas.append(nota)
	else:
		asignaturas.remove(i)

print('\nDebes repetir: ')
for i in range(len(asignaturas)):
	print(asignaturas[i], ': ', notas[i])



asignaturas = ["Matemáticas", "Física", "Química", "Historia", "Lengua"]
asignaturasSuspendidas = asignaturas.copy();
for i in asignaturas:
    nota = int(input("Nota en la asignatura " + i +":"))
    if (nota >= 5):
        asignaturasSuspendidas.remove(i)
print("Asignaturas suspendidas "+str(asignaturasSuspendidas))


