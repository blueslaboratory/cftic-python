# Ejercicios de Listas y Tuplas
# Day 4 - 02/06/2023


'''
Ejercicio 7
Escribir un programa que almacene el abecedario en una lista, elimine de la
lista las letras que ocupen posiciones múltiplos de 3, y muestre por pantalla la
lista resultante.
'''

print('\n*** EJERCICIO 7 ***')
print('\nMi solucion: ')

abecedario = list('abcdefghijklmnñopqrstuvwxyz')
indices = []

for i in range(len(abecedario)):
	indices.append(str(i))

lenAbc = len(abecedario)

'''
ChatGPT:

len(frase) - 1: len(frase) devuelve la longitud de la secuencia frase. 
Al restar 1, obtenemos el índice del último elemento de la secuencia. 
El bucle comienza desde este índice y se mueve hacia atrás.

-1: Este es el límite inferior para el índice. El bucle continúa hasta que el 
índice alcanza o supera este valor. En este caso, -1 indica que el bucle 
debe continuar hasta el índice 0 (el primer elemento de la secuencia).

-1: Este es el paso de iteración del bucle. En cada iteración, el índice se 
decrementa en 1, lo que permite recorrer la secuencia en sentido inverso.
'''

# Ir de atras hacia adelante quita problemas a la hora de reducir la lista
for i in range(lenAbc-1, -1, -1):
	if (i+1)%3 == 0:
		abecedario.pop(i)
		lenAbc-=1

# Mostrar la lista resultante
print(indices)
print(abecedario)



# Forma elegante: CHATGPT
print('\nForma elegante: CHATGPT')

abecedario = list('abcdefghijklmnñopqrstuvwxyz')
indices = []

for i in range(len(abecedario)):
	indices.append(str(i))

# Eliminar letras en posiciones multiplos de 3
n = len(abecedario)
# Posicion inicial (0-indexed) que es multiplo de 3
i = 2


while i < n:
	indices.pop(i)
	abecedario.pop(i)

	# Actualizar el size de la lista
	n -= 1

	# Incrementar el paso a 2 para saltar la letra eliminada
	i += 2

# Mostrar la lista resultante
print(indices)
print(abecedario)