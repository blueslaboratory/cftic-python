# Day 20 - 26/06/2023
# Ejercicios de Pruebas Unitarias.docx

# EN VISUALCODE COMO NO TENGAS:
# 'test_': no te lo coge como pruebas


'''
Ejercicio 10  Divisores de un Número
Escribe una función divisores(numero: int) -> List[int] que tome un número entero
y devuelva una lista con todos sus divisores.
'''

# SOLUCION PROFE

import unittest
from typing import List


def divisores0(numero: int) -> List[int]:
	lista_divisores = []
	for num in range(1, numero + 1):
		if numero % num == 0:
			lista_divisores.append(num)
	return lista_divisores


def divisores(numero: int) -> List[int]:
	return [num for num in range(1, numero + 1) if numero % num == 0]


class PruebasDivisores(unittest.TestCase):
	def test_divisores(self):
		self.assertEqual(divisores(10), [1, 2, 5, 10])
		self.assertEqual(divisores(16), [1, 2, 4, 8, 16])
		self.assertEqual(divisores(7), [1, 7])

	def test_divisores0(self):
		self.assertEqual(divisores0(10), [1, 2, 5, 10])
		self.assertEqual(divisores0(16), [1, 2, 4, 8, 16])
		self.assertEqual(divisores0(7), [1, 7])



# Para ejecutar el Test en este cuaderno
loader = unittest.TestLoader()

suite = loader.loadTestsFromTestCase(PruebasDivisores)
# suite = unittest.TestSuite()
# suite.addTest(loader.loadTestsFromTestCase(PruebasDivisores))

runner = unittest.TextTestRunner(verbosity=2)
result = runner.run(suite)

# Para ejecutarlo en un proyecto
# if __name__ == '__main__':
# 	unittest.main()