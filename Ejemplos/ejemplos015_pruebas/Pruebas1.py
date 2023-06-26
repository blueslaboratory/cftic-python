# Day 20 - 24/06/2023
# Pruebas unitarias.docx

import unittest

class PruebaSuma(unittest.TestCase):
	def test_suma_positiva(self):
		resultado = 2 + 3
		self.assertEqual(resultado, 5, "La suma es incorrecta")

	def test_suma_negativa(self):
		resultado = 2 + (-3)
		self.assertEqual(resultado, -1, "La suma es incorrecta")


class PruebaResta(unittest.TestCase):
	def test_resta_positiva(self):
		resultado = 5 - 3
		self.assertEqual(resultado, 2, "La resta es incorrecta")

	def test_resta_negativa(self):
		resultado = 2 - 5
		self.assertEqual(resultado, -3, "La resta es incorrecta")


if __name__ == '__main__':
	suite = unittest.TestSuite()

	suite.addTest(unittest.makeSuite(PruebaSuma))
	suite.addTest(unittest.makeSuite(PruebaResta))

	unittest.TextTestRunner().run(suite)


# Sin el deprecated
if __name__ == '__main__':
	loader = unittest.TestLoader()
	suite = unittest.TestSuite()
	suite.addTest(loader.loadTestsFromTestCase(PruebaSuma))

	# Estas líneas no son opcionales si deseas ejecutar las pruebas automáticamente
	# al ejecutar el archivo directamente:
	runner = unittest.TextTestRunner()
	runner.run(suite)