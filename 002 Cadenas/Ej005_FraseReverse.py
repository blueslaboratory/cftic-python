# Ejercicios de Cadenas
# Day 2 - 31/05/2023

'''
Ejercicio 5
Escribir un programa que pida al usuario que introduzca una frase en la consola y
muestre por pantalla la frase invertida.
'''

print('\n *** EJERCICIO 5 ***')

frase = input('Frase: ')
print('\nForma 1:')
print('Frase reverse: ', frase[::-1])



# Forma 2
print('\nForma 2:')
print('Frase reverse: ', ''.join(reversed(frase)))



# Forma 3
print('\nForma 3:')
fraseInvertida = ''


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

for i in range(len(frase)-1, -1, -1):
	fraseInvertida += frase[i]
	print(i, frase[i], fraseInvertida)



# Letra a letra
print('\nForma 1 - Letra a letra:')
fraseNoInvertida = ''

for i in range(len(frase)):
	fraseNoInvertida += frase[i]
	print(i, frase[i], fraseNoInvertida)



print('\nForma 2 - Letra a letra:')
fraseNoInvertida = ''

for i in range(0, len(frase), 1):
	fraseNoInvertida += frase[i]
	print(i, frase[i], fraseNoInvertida)
