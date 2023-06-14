# Day 12 - 14/06/2023
# Ejercicios de Ficheros


'''
Ejercicio 4
Escribir un programa que acceda a un fichero de internet mediante su url y 
muestre por pantalla el número de palabras que contiene.

https://www.gutenberg.org/files/2000/2000-0.txt
'''


print('\n*** EJERCICIO 4 - SOLUCION PROFE ***')

from urllib import request
from urllib.error import URLError


def contar_palabras(url):
    try:
        f = request.urlopen(url)
    except  URLError:
        return('La url no existe')
    else:
        contenido = f.read()
        return len(contenido.split())


print(contar_palabras('https://www.gutenberg.org/files/2000/2000-0.txt'))
print(contar_palabras('https://no-existe.txt'))