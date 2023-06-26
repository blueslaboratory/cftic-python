# Day 20 - 26/06/2023
# Ejercicios de Pruebas Unitarias.docx

# EN VISUALCODE COMO NO TENGAS:
# 'test_': no te lo coge como pruebas


'''
Ejercicio 4: Prueba de igualdad aproximada
Escribe una función calcular_area_circulo(radio) que tome como argumento el
radio de un círculo y devuelva el área correspondiente. Escribe una prueba unitaria
para esta función, verificando si el resultado es igual a 50.265 aproximadamente.
'''

# SOLUCION PROFE

import unittest
import math


def calcular_area_circulo(radio):
    return math.pi * radio**2


class TestCalcularAreaCirculo(unittest.TestCase):
    def test_calcular_area_circulo(self):
        self.assertAlmostEqual(calcular_area_circulo(4), 50.265, places=3)


# Para ejecutar el Test en este cuaderno
loader = unittest.TestLoader()

suite = loader.loadTestsFromTestCase(TestCalcularAreaCirculo)
# suite = unittest.TestSuite()
# suite.addTest(loader.loadTestsFromTestCase(TestCalcularAreaCirculo))

runner = unittest.TextTestRunner(verbosity=2)
result = runner.run(suite)

# Para ejecutarlo en un proyecto
# if __name__ == '__main__':
#    unittest.main()