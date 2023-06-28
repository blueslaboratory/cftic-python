# Day 22 - 27/06/2023
# Trazas.docx (CTRL+C & CTRL+V)

import logging

__LOG = logging.getLogger('ambos')

def _log():
    return logging.getLogger('ambos')

def sumar0(a,b):
	# te lee el archivo de configuracion y te coge el gestor root
	logger=logging.getLogger('root')
	# esto te saldria por consola: el handler de root es consola
	logger.info(f'sumar0 {a} + {b}')
	return a+b

def sumar1(a,b):
    _log().info(f'sumar1 {a} + {b}')
    return a+b

# asi es como se debe hacer:
def sumar2(a,b):
    __LOG.info(f'[sumar2]')
    __LOG.debug(f'[params][a:{a}][b:{b}]')
    resultado = a+b
    __LOG.debug(f'[resultado:{resultado}]')
    return resultado

def restar(a,b):
    # te lee el archivo de configuracion y te coge el gestor sampleLogger
	logger = logging.getLogger('sampleLogger')
	# esto te saldria por sample.log: el handler de sampleLogger es fileHandler
	logger.info(f'restar {a} - {b}')
	return a-b

def multiplicar(a,b):
	logger = logging.getLogger('ambos')
	logger.info(f'multiplicar0 {a} * {b}')
	return a*b

def dividir(a,b):
	logger = logging.getLogger('ambos')
	logger.info(f'dividir0 {a} / {b}')
	return a/b