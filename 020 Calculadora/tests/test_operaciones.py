# Day 22 - 27/06/2023

import unittest
import calculadora.operaciones as op


class TestOperaciones(unittest.TestCase):
    
    
    # Test de sumar:
    def test_sumar(self):
        self.assertEqual(op.sumar0(2,2), 4)
        self.assertEqual(op.sumar1(2,2), 4)
        self.assertEqual(op.sumar2(2,2), 4)
    
    
    # Test de restar:
    def test_restar_positive(self):
        # positive test case
        result = op.restar(5, 3)
        self.assertEqual(result, 2)

    def test_restar_negative(self):
        # negative test case
        result = op.restar(-5, 3)
        self.assertEqual(result, -8)

    def test_restar_error(self):
        # error test case
        with self.assertRaises(TypeError):
            op.restar("5", 3)

    def test_restar_edge(self):
        # edge test case
        result = op.restar(0, 0)
        self.assertEqual(result, 0)