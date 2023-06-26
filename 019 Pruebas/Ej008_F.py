# Day 20 - 26/06/2023
# Ejercicios de Pruebas Unitarias.docx

# EN VISUALCODE COMO NO TENGAS:
# 'test_': no te lo coge como pruebas


'''
Ejercicio 8  Suma de Números Pares
Escribe una función sumar_pares(n: int) -> int que sume todos los números pares
desde 1 hasta n (incluyendo n si es par).
'''

# SOLUCION PROFE
import unittest


def sumar_pares0(n: int) -> int:
	numeros_pares = []

	for num in range(1, n+1):
		if num % 2 == 0:
			numeros_pares.append(num)

	suma = sum(numeros_pares)

	return suma


def sumar_pares(n: int) -> int:
	return sum([num for num in range(1, n + 1) if num % 2 == 0])

class PruebasSumarPares(unittest.TestCase):
	def test_sumar_pares(self):
		self.assertEqual(sumar_pares0(10), 30) # 10,0,8,2,6,4 --> 10*3
		self.assertEqual(sumar_pares0(15), 56) # 14,0,12,2,10,4,8,6 --> 14*4
		self.assertEqual(sumar_pares(10), 30)
		self.assertEqual(sumar_pares(15), 56)


# Para ejecutar el Test en este cuaderno
loader = unittest.TestLoader()

suite = loader.loadTestsFromTestCase(PruebasSumarPares)
# suite = unittest.TestSuite()
# suite.addTest(loader.loadTestsFromTestCase(PruebasSumarPares))

runner = unittest.TextTestRunner(verbosity=2)
result = runner.run(suite)

# Para ejecutarlo en un proyecto
# if __name__ == '__main__':
# 	unittest.main()