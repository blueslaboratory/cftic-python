# Day 20 - 26/06/2023
# Ejercicios de Pruebas Unitarias.docx

# EN VISUALCODE COMO NO TENGAS:
# 'test_': no te lo coge como pruebas


'''
Ejercicio 9 Ordenar Palabras
Escribe una función ordenar_palabras(palabras: List[str]) -> List[str] que tome
una lista de palabras y las ordene en orden alfabético, ignorando las mayúsculas
y minúsculas.
'''

# SOLUCION PROFE: CORREGIDO EN CLASE

import logging
import unittest
from typing import List


def ordenar_palabras(palabras: List[str]) -> List[str]:
	return sorted(palabras, key=str.lower)


def ordenar_lista(lista:list[str]) -> list[str]:
	lista_minusculas = [x.lower() for x in lista]
	lista_ordenada = sorted(lista_minusculas)
	return lista_ordenada


class MiObjeto():
	def __init__(self, nombre):
		self.nombre = nombre

	def __eq__(self, obj):
		# True: el objeto que viene tiene el mismo nombre que yo
		return self.nombre==obj.nombre

	def __str__(self):
		return f'MiObjeto {self.nombre}'

def mifuncion():
	return MiObjeto('Maria')


class PruebasOrdenarPalabras(unittest.TestCase):
	logging.basicConfig(level=logging.DEBUG,
						filename='misTrazas.log',
						format='%(asctime)s - %(levelname)s - %(message)s')


	lista = ['hola', 'pepe', 'alba', 'adios', 'viva', 'madrid']
	lista_ordenada = ['adios', 'alba', 'hola', 'madrid', 'pepe', 'viva']

	def test_ordenar_palabras(self):
		palabras = ['Manzana', 'banana', 'cereza', 'dátil']
		resultado = ordenar_palabras(palabras)
		self.assertEqual(resultado, ['banana', 'cereza', 'dátil', 'Manzana'])


	objeto = MiObjeto('Maria')

	def test_1(self):
		self.assertEqual(ordenar_lista(self.lista), self.lista_ordenada)
		# Metiendo trazas: misTrazas.log
		# .debug no es un print
		logging.info('{Ej009_ListaOrdenada}-{test_1}')
		logging.debug('Mi carro me lo robaron')
		logging.info('pero lo han devuelto')
		logging.debug(MiObjeto('Pepe'))

	def test_Objetos(self):
		self.assertEqual(mifuncion(), self.objeto)


'''
# Para ejecutar el Test en este cuaderno
loader = unittest.TestLoader()

suite = loader.loadTestsFromTestCase(PruebasOrdenarPalabras)
# suite = unittest.TestSuite()
# suite.addTest(loader.loadTestsFromTestCase(PruebasOrdenarPalabras))

runner = unittest.TextTestRunner(verbosity=2)
result = runner.run(suite)
'''

# Para ejecutarlo en un proyecto
if __name__ == '__main__':
	unittest.main()