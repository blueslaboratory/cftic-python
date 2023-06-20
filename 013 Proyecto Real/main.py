# Day 14 - 16/06/2023
# Ejercicios Mix

# El main.py seria la capa de presentacion


from dao.Ej001_ConnectionManager import ConexionMySQL
from ln.Ej001_AlmacenarInformacion import AlmacenarInformacion
from ln.errors.Ej001_ErrorsLN import ErrorLN


if __name__ == '__main__':
	try:
		# nombre_fichero = input('Nombre fichero: ')

		# Para cuando no importas la clase:
		# Ej001_AlmacenarInformacion.AlmacenarInformacion.almacenar_persona(nombre_fichero)

		# Para cuando importas la clase:
		# se hace asi porque no hay metodos estaticos, tienes que crear el objeto
		almacenarInformacion = AlmacenarInformacion()
		# AlmacenarInformacion.almacenar_persona(nombre_fichero)
		almacenarInformacion.almacenar_persona('datos.csv')

		print('El proceso se ha ejecutado correctamente')

	# asignar el objeto ErrorLN como eln
	except ErrorLN as eln:
		print(eln.__cause__)

	except:
		print('Se ha producido un error de sitema')

