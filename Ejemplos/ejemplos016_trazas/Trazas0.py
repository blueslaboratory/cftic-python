# Day 21 - 27/06/2023
# Trazas.docx
# Las trazas son los logs

import logging

# Configuracion basica de registro
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(levelname)s - %(message)s')

# Ejemplo de uso
logging.debug('Este es un mensaje de depuración')
logging.info('Esta es una información')
logging.warning('¡Cuidado!')
logging.error('Ocurrió un error')