# Ejercicios de Condicionales
# Day 4 - 02/06/2023


'''
Ejercicio 6
Los alumnos de un curso se han dividido en dos grupos A y B de acuerdo al sexo y el
nombre. El grupo A esta formado por las mujeres con un nombre anterior a la M y los
hombres con un nombre posterior a la N y el grupo B por el resto.
Escribir un programa que pregunte al usuario su nombre y sexo, y muestre por pantalla
el grupo que le corresponde.
'''

print('\n*** EJERCICIO 6 ***')

sexo = input('Sexo (M/F): ')
nombre = input('Nombre: ')

if(sexo.lower() == 'f'):
	if(nombre[0].upper() < 'M'):
		print('Grupo A: mujer')
	else:
		print('Grupo B: mujer')
elif(sexo.lower() == 'm'):
	if (nombre[0].upper() > 'N'):
		print('Grupo A: hombre')
	else:
		print('Grupo B: hombre')
else:
	print('Genero no reconocido')



print('\n*** EJERCICIO 6 - SOLUCION PROFE ***')

nombre = input("Dame nombre: ").upper()
sexo = input("Dame sexo (H/M): ").upper()
grupo = "Ninguno"

if nombre < "M" and sexo == "M":
	grupo = "A"
elif nombre > "N" and sexo == "H":
	grupo = "A"
else:
	grupo = "B"

print("El grupo es " +grupo)



########################################################
# Otra solucion
########################################################
print('\n*** EJERCICIO 6 - SOLUCION PROFE 2 ***')

VALORES_MUJER = 'MUJER'
VALORES_HOMBRE = 'HOMBRE'
nombre = input("Dame nombre: ").upper()
sexo = input("Dame sexo (H/M): ").upper()

# find() devuelve -1 cuando no encuentra la subcadena especificada
isMujer = VALORES_MUJER.find(sexo) != -1;
isHombre = VALORES_HOMBRE.find(sexo) != -1;

grupo= 'B'
if (nombre[0] < "M" and isMujer) or (nombre[0] > "N" and isHombre):
   grupo = "A"


print("El grupo es", grupo)



########################################################
# Otra solucion
########################################################
print('\n*** EJERCICIO 6 - SOLUCION PROFE 3 ***')

VALORES_MUJER = ('M','MUJER')
VALORES_HOMBRE = ('H','HOMBRE')
nombre = input("Dame nombre: ").upper()
sexo = input("Dame sexo (H/M): ").upper()

isMujer= sexo in VALORES_MUJER;
isHombre = sexo in VALORES_HOMBRE;

grupo= 'B'
if (nombre[0] < "M" and isMujer) or (nombre[0] > "N" and isHombre):
   grupo = "A"


print("El grupo es", grupo)