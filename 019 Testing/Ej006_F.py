# Day 20 - 26/06/2023
# Ejercicios de Pruebas Unitarias.docx

# EN VISUALCODE COMO NO TENGAS:
# 'test_': no te lo coge como pruebas


'''
Ejercicio 6  Validar Palíndromos
Escribe una función es_palindromo(palabra: str) -> bool que tome una cadena de
caracteres y determine si es un palíndromo (se lee igual de izquierda a derecha y
de derecha a izquierda). Ignora los espacios en blanco y considera que la comparación
no distingue entre mayúsculas y minúsculas.
'''

# SOLUCION PROFE

import unittest


def es_palindromo(palabra: str) -> bool:
    palabra = palabra.replace(' ', '').lower()
    return palabra == palabra[::-1]


class PruebasPalindromo(unittest.TestCase):
    def test_palindromo(self):
        self.assertTrue(es_palindromo('Anita lava la tina'))
        self.assertTrue(es_palindromo('Able was I ere I saw Elba'))
        self.assertFalse(es_palindromo('Hola mundo'))


# Para ejecutar el Test en este cuaderno
loader = unittest.TestLoader()

suite = loader.loadTestsFromTestCase(PruebasPalindromo)
# suite = unittest.TestSuite()
# suite.addTest(loader.loadTestsFromTestCase(PruebasPalindromo))

runner = unittest.TextTestRunner(verbosity=2)
result = runner.run(suite)

# Para ejecutarlo en un proyecto
# if __name__ == '__main__':
# 	unittest.main()