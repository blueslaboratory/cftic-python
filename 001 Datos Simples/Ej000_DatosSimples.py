# Ejercicios Datos Simples
# Day 1 - 30/05/2023


"""
Ejercicio 1
Escribir un programa que muestre por pantalla la cadena ¡Hola Mundo!.
"""

print('\n *** EJERCICIO 1 ***')
print('¡Hola Mundo!')



"""
Ejercicio 2
Escribir un programa que almacene la cadena ¡Hola Mundo! en una
variable y luego muestre por pantalla el contenido de la variable.
"""

print('\n *** EJERCICIO 2 ***')
mensaje = '¡Hola Mundo!'
print(mensaje)



"""
Ejercicio 3
Escribir un programa que pregunte el nombre del usuario en la consola
y después de que el usuario lo introduzca muestre por pantalla la cadena
¡Hola <nombre>!, donde <nombre> es el nombre que el usuario haya introducido.
"""

print('\n *** EJERCICIO 3 ***')
nombre = input('Introduce tu nombre: ')
print('¡Hola ' +nombre +'!')

# Varias soluciones
print('¡Hola ', nombre, '!', sep='')
print('¡Hola', nombre, end='!\n')
print(f'¡Hola {nombre}!')
print('¡Hola %s!' % nombre)
print('¡Hola {0}!'.format(nombre))



"""
Ejercicio 4
Escribir un programa que muestre por pantalla el resultado de la siguiente operación 
aritmética: ((3+2)/(2*5))^2
"""

print('\n *** EJERCICIO 4 ***')
operacion = ((3+2)/(2*5))**2
print('El resultado es:', operacion)



"""
Ejercicio 5
Escribir un programa que pregunte al usuario por el número de horas trabajadas y el 
coste por hora. Después debe mostrar por pantalla la paga que le corresponde.
"""

print('\n *** EJERCICIO 5 ***')
horas = int(input('Introduce las horas trabajadas: '))
satoshisPorHora = float(input('Introduce tu precio por hora (丰):' ))
paga = horas*satoshisPorHora
print('Paga correspondiente concatenacion: ' +str(paga))
print('Paga correspondiente con coma: ', paga)



"""
Ejercicio 6
Escribir un programa que lea un entero positivo, introducido por el usuario y después muestre
en pantalla la suma de todos los enteros desde 1 hasta n..
La suma de los primeros enteros positivos puede ser calculada de la siguiente forma:
suma = n(n+1)/2
"""

print('\n *** EJERCICIO 6 ***')
n = int(input('Introduce un entero positivo: '))
# division entera 1
suma = int(n*(n+1)/2)
# division entera 2
suma = n*(n+1)//2
print('Suma de los primeros enteros positivos de 1 hasta ' +str(n) +': ' +str(suma))



"""
Ejercicio 7
Escribir un programa que pida al usuario su peso (en kg) y estatura (en metros), calcule el
índice de masa corporal (IMC) y lo almacene en una variable, y muestre por pantalla la frase:
Tu índice de masa corporal es <imc> donde <imc> es el índice de masa corporal calculado
redondeado con dos decimales.
Cálculo de imc: consiste en dividir el peso, expresado en kilos, entre la estatura,
en metros, elevada al cuadrado (kg/m^2)
"""

print('\n *** EJERCICIO 7 ***')
masa = float(input('Masa corporal (kg): '))
estatura = float(input('Estatura (m): '))

IMC = masa/(estatura**2)
IMC_rounded = round(IMC, 2)

print('IMC = ' , IMC_rounded)



"""
Ejercicio 8
Escribir un programa que pida al usuario dos números enteros y muestre por pantalla
“La división de <n> entre <m> da un cociente <c> y un resto <r>” donde <n> y <m> son
los números introducidos por el usuario, y <c> y <r> son el cociente y el resto de la división
entera respectivamente.
"""

print('\n *** EJERCICIO 8 ***')
n1 = int(input('Numero entero 1: '))
n2 = int(input('Numero entero 2: '))

cociente = int(n1/n2)
resto = n1%n2

print('La division de ' +str(n1) +' entre ' +str(n2)
      +' da un cociente ' +str(cociente)
      +' y un resto de ' +str(resto))



"""
Ejercicio 9
Escribir un programa que pregunte al usuario una cantidad a invertir, el interés anual y
el número de años, y muestre por pantalla el capital obtenido en la inversión.

Capital final = Capital*(1 + Tasa de interés/100)^Tiempo
"""

print('\n *** EJERCICIO 9 ***')
cantidad = float(input('Cantidad a invertir: '))
interes = float(input('Interes anual (%): '))
years = int(input('Años de inversion: '))

capital = cantidad*(1+interes/100)**years

print('El capital obtenido en la inversion es: ', capital)



# ME QUEDO POR AQUI

"""
Ejercicio 10
Una juguetería tiene mucho éxito en dos de sus productos: payasos y muñecas. Suele hacer
venta por correo y la empresa de logística les cobra por peso de cada paquete así que deben
calcular el peso de los payasos y muñecas que saldrán en cada paquete a demanda. Cada
payaso pesa 112 g y cada muñeca 75 g. Escribir un programa que lea el número de payasos y
muñecas vendidos en el último pedido y calcule el peso total del paquete que será enviado.
"""

"""
Ejercicio 11
Imagina que acabas de abrir una nueva cuenta de ahorros que te ofrece el 4% de interés
al año. Estos ahorros debido a intereses, que no se cobran hasta finales de año, se te
añaden al balance final de tu cuenta de ahorros. Escribir un programa que comience leyendo
la cantidad de dinero depositada en la cuenta de ahorros, introducida por el usuario.
Después el programa debe calcular y mostrar por pantalla la cantidad de ahorros tras el
primer, segundo y tercer años. Redondear cada cantidad a dos decimales.
"""


"""
Ejercicio 12
Una panadería vende barras de pan a 3.49€ cada una. El pan que no es del día tiene un
descuento del 60%. Escribir un programa que comience leyendo el número de barras vendidas
que no son del día. Después el programa debe mostrar el precio habitual de una barra de pan,
el descuento que se le hace por no ser fresca y el coste final total.
"""
