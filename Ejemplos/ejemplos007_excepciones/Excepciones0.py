# Day 8 - 08/06/2023

# Gestión de Excepciones.docx
# Toda excepcion extiende de BaseException

# Bloque: try - except - else - finally:

try:
	# Lanzar la excepcion
	# Bloque de codigo donde puede ocurrir una excepcion
	x = int(input("Ingresa un numero: "))
	resultado = 10 / x

except ValueError:
	# Except es como el catch de java, puede haber [1,n] excepts
	# Excepcion ValueError: cualquier valor que no pueda convertirse en un entero
	print("Error: Ingresaste un valor no numerico.")

except ZeroDivisionError:
	# Except es como el catch de java, puede haber [1,n] excepts
	# Excepcion ZeroDivisionError
	print("Error: No es posible dividir entre cero.")

except BaseException:
	# La Excepcion padre, hay que poner los hijos antes que los padres
	print("Se ha producido un error general")

else:
	# Este bloque se ejecuta si no se produce ninguna excepcion
	# Solo puede haber un bloque [0,1] elses
	print("El resultado es:", resultado)

finally:
	# Este bloque siempre se ejecuta, independientemente de si hay una excepcion o no
	# Solo puede haber un bloque [0,1] finally
	print("¡Fin del programa!")