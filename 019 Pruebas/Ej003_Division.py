# Day 20 - 26/06/2023
# Ejercicios de Pruebas Unitarias.docx

# EN VISUALCODE COMO NO TENGAS:
# 'test_': no te lo coge como pruebas


'''
Ejercicio 3: Prueba de lanzamiento de excepción
Escribe una función dividir(a, b) que tome como argumentos dos números y devuelva
el resultado de dividir a entre b. Si b es igual a cero, la función debe lanzar
una excepción ZeroDivisionError. Escribe una prueba unitaria para esta función.
'''

# SOLUCION PROFE

import unittest


def dividir(a, b):
    if b == 0:
        raise ZeroDivisionError("No se puede dividir por cero")
    return a / b


class TestDividir(unittest.TestCase):
    def test_dividir(self):
        self.assertEqual(dividir(10, 2), 5)
        self.assertEqual(dividir(8, 4), 2)
        self.assertRaises(ZeroDivisionError, dividir, 10, 0)


# Para ejecutar el Test en este cuaderno:

loader = unittest.TestLoader()

suite = loader.loadTestsFromTestCase(TestDividir)
# suite = unittest.TestSuite()
# suite.addTest(loader.loadTestsFromTestCase(TestDividir))

runner = unittest.TextTestRunner(verbosity=2)
result = runner.run(suite)

# Para ejecutarlo en un proyecto
# if __name__ == '__main__':
# 	unittest.main()