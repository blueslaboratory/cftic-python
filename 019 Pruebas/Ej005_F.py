# Day 20 - 26/06/2023
# Ejercicios de Pruebas Unitarias.docx

# EN VISUALCODE COMO NO TENGAS:
# 'test_': no te lo coge como pruebas


'''
Ejercicio 5: Prueba de cadena vacía
Escribe una función es_cadena_vacia(cadena) que tome como argumento una cadena de
texto y devuelva True si la cadena está vacía (no contiene ningún carácter), y False
en caso contrario. Escribe una prueba unitaria para esta función.
'''

# SOLUCION PROFE

import unittest


def es_cadena_vacia(cadena):
    return len(cadena) == 0


class TestEsCadenaVacia(unittest.TestCase):
    def test_es_cadena_vacia(self):
        self.assertTrue(es_cadena_vacia(""))
        self.assertFalse(es_cadena_vacia("Hola"))
        self.assertFalse(es_cadena_vacia(" "))


# Para ejecutar el Test en este cuaderno
loader = unittest.TestLoader()

suite = loader.loadTestsFromTestCase(TestEsCadenaVacia)
# suite = unittest.TestSuite()
# suite.addTest(loader.loadTestsFromTestCase(TestEsCadenaVacia))

runner = unittest.TextTestRunner(verbosity=2)
result = runner.run(suite)

# Para ejecutarlo en un proyecto
# if __name__ == '__main__':
# 	unittest.main()