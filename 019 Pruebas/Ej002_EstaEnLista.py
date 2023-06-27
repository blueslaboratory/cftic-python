# Day 20 - 26/06/2023
# Ejercicios de Pruebas Unitarias.docx

# EN VISUALCODE COMO NO TENGAS:
# 'test_': no te lo coge como pruebas


'''
Ejercicio 2 Prueba de pertenencia en lista
Escribe una función esta_en_lista(elemento, lista) que tome como argumentos un
elemento y una lista, y devuelva True si el elemento está presente en la lista,
y False en caso contrario. Escribe una prueba unitaria para esta función.
'''

# SOLUCION PROFE: CORREGIDO EN CLASE

import unittest


def esta_en_lista(elemento, lista):
	try:
		return elemento in lista
	except TypeError:
		return False
	except: #except BaseException
		return False


class TestEstaEnLista(unittest.TestCase):
	lista = [1,2,3,4,5]

	def test_esta_en_lista(self):
		self.assertTrue(esta_en_lista(3, [1, 2, 3, 4, 5]))
		self.assertFalse(esta_en_lista(6, self.lista))
		self.assertTrue(esta_en_lista('a', ['a', 'b', 'c']))
		self.assertFalse(esta_en_lista('d', ['a', 'b', 'c']))

	def test_no_esta_en_lista(self):
		self.assertEqual(esta_en_lista(7, self.lista), False)


# Para ejecutar el Test en este cuaderno
loader = unittest.TestLoader()

# suite = loader.loadTestsFromTestCase(TestEstaEnLista)
suite = unittest.TestSuite()
suite.addTest(loader.loadTestsFromTestCase(TestEstaEnLista))

runner = unittest.TextTestRunner(verbosity=2)
result = runner.run(suite)

#Para ejecutarlo en un proyecto
#if __name__ == '__main__':
#    unittest.main(verbosity=2)
