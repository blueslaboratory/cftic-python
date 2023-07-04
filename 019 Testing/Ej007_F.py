# Day 20 - 26/06/2023
# Ejercicios de Pruebas Unitarias.docx

# EN VISUALCODE COMO NO TENGAS:
# 'test_': no te lo coge como pruebas


'''
Ejercicio 7 Contar Ocurrencias
Escribe una función contar_ocurrencias(lista: List[int], elemento: int) -> int que
tome una lista de enteros y cuente cuántas veces aparece un elemento específico en
ella.
'''

# SOLUCION PROFE
import unittest
from typing import List


def contar_ocurrencias(lista: List[int], elemento: int) -> int:
    return lista.count(elemento)


class PruebasContarOcurrencias(unittest.TestCase):
    def test_contar_ocurrencias(self):
        self.assertEqual(contar_ocurrencias([1, 2, 3, 4, 4, 4, 5], 4), 3)
        self.assertEqual(contar_ocurrencias([1, 2, 3, 4, 5], 6), 0)


# Para ejecutar el Test en este cuaderno
loader = unittest.TestLoader()

suite = loader.loadTestsFromTestCase(PruebasContarOcurrencias)
# suite = unittest.TestSuite()
# suite.addTest(loader.loadTestsFromTestCase(PruebasContarOcurrencias))

runner = unittest.TextTestRunner(verbosity=2)
result = runner.run(suite)

# Para ejecutarlo en un proyecto
# if __name__ == '__main__':
# 	unittest.main()