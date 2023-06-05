# Day 5 - 05/06/2023
# Funciones de usuario.docx



print('\n*** Parametros de entrada ***')
def saludo(nombre):
	print("Hola, " + nombre)

saludo("Juan")



print('\n*** Parametros con nombre ***')
def saludar(nombre, mensaje):
	print(f"Hola {nombre}, {mensaje}")

saludar(mensaje="bienvenido", nombre="Juan")



print('\n*** Parametros por defecto ***')
def saludar(nombre, mensaje="bienvenido"):
	print(f"Hola {nombre}, {mensaje}")


saludar("Juan")
# Salida: Hola Juan, bienvenido
saludar("Pedro", "hola")
# Salida: Hola Pedro, hola



print('\n*** Parametros variables posicionales ***')
'''
Se denotan con un asterisco (*) antes del nombre del parámetro y permiten pasar 
un número variable de argumentos posicionales. Los argumentos se agruparán en una 
tupla dentro de la función. 
'''
def sumar(*numeros):
    total = sum(numeros)
    print(f"La suma es: {total}")

sumar(1, 2, 3)
# Salida: La suma es: 6
sumar(4, 5, 6, 7)
# Salida: La suma es: 22



print('\n*** Parametros variables con nombre ***')
def imprimir_datos(**datos):
    for clave, valor in datos.items():
        print(f"{clave}: {valor}")

imprimir_datos(nombre="Juan", edad=30)
# Salida: nombre: Juan\nedad: 30
imprimir_datos(nombre="Pedro", ocupacion="ingeniero", ciudad="Madrid")
# Salida: nombre: Pedro\nocupacion: ingeniero\nciudad: Madrid



print('\n*** Valor de retorno ***')
def suma(a, b):
    return a + b

resultado = suma(5, 3)
# Llama a la función suma con los argumentos 5 y 3
print(resultado)
# Imprime el resultado de la suma: 8



print('\n*** Variables locales y globales ***')
global_variable = 10

def function():
    local_variable = 5
    global global_variable

    global_variable += local_variable
    print(global_variable)

function()
# Imprime 15



print('\n*** Documentación de la función ***')
def suma(a, b):
    """
    Esta función realiza la suma de dos números.

    Parámetros:
    a (int): El primer número.
    b (int): El segundo número.

    Retorna:
    int: El resultado de la suma.
    """
    return a + b

# Imprime la documentación de la función suma
print(suma.__doc__)