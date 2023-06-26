# Day 20 - 26/06/2023
# Ejercicios de Pruebas Unitarias.docx

# EN VISUALCODE COMO NO TENGAS:
# 'test_': no te lo coge como pruebas


'''
Ejercicio 1 Prueba de igualdad
Escribe una función es_mayor_de_edad(edad) que tome como argumento un entero
que representa la edad de una persona y devuelva True si es mayor o igual a 18,
y False en caso contrario. Escribe una prueba unitaria para esta función.
'''

import unittest


def esMayorEdad(edad):
	if (edad >= 18):
		return True
	else:
		return False


def es_mayor_de_edad(edad):
	return edad >= 18


class TestEsMayorDeEdad(unittest.TestCase):

	def test_es_mayor_de_edad0(self):
		# self.assertTrue(esMayorEdad(7))
		self.assertTrue(esMayorEdad(18))
		# self.assertFalse(esMayorEdad(99))
		self.assertFalse(esMayorEdad(14))

	def test_es_mayor_de_edad1(self):
		self.assertTrue(es_mayor_de_edad(18))
		self.assertTrue(es_mayor_de_edad(21))
		self.assertFalse(es_mayor_de_edad(16))
		self.assertFalse(es_mayor_de_edad(17))

	def test_es_cadena(self):
		with self.assertRaises(TypeError):
			es_mayor_de_edad('a')

	def test_es_vacio_edad(self):
		with self.assertRaises(TypeError):
			es_mayor_de_edad()

	def test_es_nulo_edad(self):
		with self.assertRaises(TypeError):
			es_mayor_de_edad(None)

	def test_es_espacio_valor_edad(self):
		self.assertEqual(es_mayor_de_edad( 5), False)

	def test_es_decimal(self):
		self.assertTrue(es_mayor_de_edad(18.5))
		self.assertFalse(es_mayor_de_edad(17.9))


# Para ejecutar el Test en este cuaderno
loader = unittest.TestLoader()

suite = loader.loadTestsFromTestCase(TestEsMayorDeEdad)
# suite = unittest.TestSuite()
# suite.addTest(loader.loadTestsFromTestCase(TestEsMayorDeEdad))

# verbosity=2 es la recomendada
runner = unittest.TextTestRunner(verbosity=2)
result = runner.run(suite)

# Para ejecutarlo en un proyecto
# if __name__ == '__main__':
# 	unittest.main()