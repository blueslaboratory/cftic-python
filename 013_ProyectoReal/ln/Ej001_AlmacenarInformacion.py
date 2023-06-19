# Day 14 - 16/06/2023
# Ejercicios Mix

from ln.Ej001_LecturaFichero import LecturaFichero
from ln.Ej001_TratamientoDatos import TratamientoDatos
# La sintaxis de Python no permite importar de 012 Avanzados/Ej001 Partes3/dao
# por eso he hecho una copia dentro de la carpeta de ln (Logica de Negocio)
# PERO DEBERIA DE ESTAR EN dao

# Si permite pero hay que usar rutas relativas (gracias chadGPT)
from dao.Ej001_PersonaDAO import PersonaDAO

# Importando errores
from ln.errors.Ej001_ErrorsLN import ErrorLN
from dao.errors.Ej001_ErrorsDAO import ErrorDAO


class AlmacenarInformacion:

	# Convertir una funcion a metodo, agregar self: OBLIGATORIO
	def almacenar_persona(self, nombreFichero):

		try:

			fichero = LecturaFichero(nombreFichero)
			datos_iniciales = fichero.leer_fichero()

			datos = TratamientoDatos()
			datos_finales = datos.tratar_datos(datos_iniciales)

			personaDAO = PersonaDAO()
			personaDAO.insertar_datos(datos_finales)

		except ErrorLN as eln:
			raise eln

		except ErrorDAO:
			raise ErrorLN

		except:
			raise ErrorLN('ErrorLN - Se ha producido un error general')
