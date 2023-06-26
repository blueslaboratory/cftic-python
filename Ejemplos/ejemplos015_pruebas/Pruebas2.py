# Day 20 - 24/06/2023
# Pruebas unitarias.docx

import unittest


class MiPrueba(unittest.TestCase):
    def test_igualdad(self):
        self.assertEqual(2 + 2, 4)

    def test_verdadero(self):
        self.assertTrue(5 > 2)

    def test_falso(self):
        self.assertFalse(1 > 3)

    def test_es_nulo(self):
        valor = None
        self.assertIsNone(valor)

    def test_no_es_nulo(self):
        valor = 42
        self.assertIsNotNone(valor)

    def test_contenido(self):
        lista = [1, 2, 3, 4, 5]
        self.assertIn(3, lista)

    def test_no_contenido(self):
        lista = [1, 2, 3, 4, 5]
        self.assertNotIn(6, lista)

    def test_excepcion(self):
        with self.assertRaises(ValueError):
            int("texto")


if __name__ == '__main__':
    unittest.main()