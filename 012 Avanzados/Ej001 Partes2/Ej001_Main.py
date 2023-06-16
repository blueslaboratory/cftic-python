# Day 14 - 16/06/2023
# Ejercicios Mix

import Ej001_LecturaFichero
import Ej001_TratamientoDatos
import Ej001_DAO


try:
	datos_iniciales = Ej001_LecturaFichero.leer_fichero('datos.csv')
	datos_finales = Ej001_TratamientoDatos.tratar_datos(datos_iniciales)
	Ej001_DAO.crear_tabla('persona')
	Ej001_DAO.insertar_datos(datos_finales)
except:
	print('Se ha producido un error en el sistema')