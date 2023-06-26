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

# SOLUCION PROFE

import unittest
from typing import List


def ordenar_palabras(palabras: List[str]) -> List[str]:
    return sorted(palabras, key=str.lower)


class PruebasOrdenarPalabras(unittest.TestCase):
    def test_ordenar_palabras(self):
        palabras = ['Manzana', 'banana', 'cereza', 'dátil']
        resultado = ordenar_palabras(palabras)
        self.assertEqual(resultado, ['banana', 'cereza', 'dátil', 'Manzana'])


# Para ejecutar el Test en este cuaderno
loader = unittest.TestLoader()

suite = loader.loadTestsFromTestCase(PruebasOrdenarPalabras)
# suite = unittest.TestSuite()
# suite.addTest(loader.loadTestsFromTestCase(PruebasOrdenarPalabras))

runner = unittest.TextTestRunner(verbosity=2)
result = runner.run(suite)

# Para ejecutarlo en un proyecto
# if __name__ == '__main__':
# 	unittest.main()