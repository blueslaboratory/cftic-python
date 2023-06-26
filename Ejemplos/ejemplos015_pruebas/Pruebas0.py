# Day 20 - 24/06/2023
# Pruebas unitarias.docx

import unittest
 
# Funcion a probar
def suma(a, b):
    return a + b
 
# Clase de prueba
class TestSuma(unittest.TestCase):
    def test_suma_positiva(self):
        resultado = suma(3, 5)
        self.assertEqual(resultado, 8)
        
    def test_prueba_fallida(self):
        resultado = suma(3, 5)
        self.assertNotEqual(resultado, 8)
 
    def test_suma_negativa(self):
        resultado = suma(-2, -7)
        self.assertEqual(resultado, -9)
 
    def test_suma_cero(self):
        resultado = suma(0, 0)
        self.assertEqual(resultado, 0)
        
 
# Ejecutar las pruebas
if __name__ == '__main__':
    unittest.main()