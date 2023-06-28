# Day 22 - 27/06/2023
# Trazas.docx (CTRL+C & CTRL+V)
# Solo funciona en VSC

import logging
import logging.config

# from operaciones import sumar, restar, multiplicar, dividir
import operaciones as op

if __name__ == '__main__':

	logging.config.fileConfig('logging.conf')
	# logger = logging.getLogger('root')

	# sumar(2,3)

	op.sumar0(2, 3)
	op.sumar1(4, 5)
	op.sumar2(6, 7)

	op.restar(99, 44)
	op.multiplicar(3, 6)
	op.dividir(27, 3)