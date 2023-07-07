# Day 29 - 07/07/2023

'''
VALIDAR CODIGO EAN

El codigo EAN (European Article Number) es un sistema de código de barras para
asignar un número único a cada producto. Los códigos más comunes tienen
8 o 13 dígitos, especialmente 13 (sistemas conocidos como EAN8 y EAN13).
En ellos van codificados el pais de origen del producto, la empresa y el propio
producto. El último de los dígitos es un dígito de control para evitar errores
de transcripción.
El algoritmo para comprobar que un código EAN8 o EAN13 ha sido transcrito
correctamente es extremadamente sencillo.

Podemos describirlo algorítmicamente de esta manera:

Comprobar que el código tiene 8 o 13 dígitos. De no ser así, no es correcto.

●Sumar los dígitos de lugares pares por un lado y los de los impares por otro,
pero sin incluir el último dígito.
●Si el código es EAN13, multiplicar la suma de los pares por 3.
●Si el código es EAN8, es la suma de los impares la que se multiplica por 3.
●Sumar el resultado de los pares y el de los impares y hallar el resto de la
división por 10.
●Realizar la operación 10 menos ese resto y ese es el dígito de control.
●Si como resultado sale 10, entenderemos que el dígito de control es 0.
●Comprobar que el dígito de control que hemos calculado y el último dígito
del código EAN coinciden

Por ejemplo, para validar el código EAN8 "12345678" (Obviamente es inventado)

1.Separar el dígito de control. Nos quedamos con "1234567" y "8"
2.Sumar pares: sumapares=2+4+6=12
3.Sumar impares: sumaimpares=1+3+5+7=16
4.Como es EAN8, multiplicamos los impares por 3.
5.sumaimpares=16*3=48
6.Sumar el resultado de pares e impares: 12+48=60
7.Hallar el resto de la division por 10: 60 mod 10 = 0
8.Hacer 10-resto: 10-0=10
9.Si el resultado del paso 8 es 10, el dígito de control es 0.
10.Comparar el dígito de control que hemos calculado con el que tenía el
código: Nos sale 0 y el código tenía un 8. Es incorrecto.

Realizar el ejercicio separando en dos clases la lógica de funcionamiento
y el  cliente.
'''

# SOLUCION PROFE

import sys

class ClaseEAN:
   def __init__(self):
      self.resultado = 0
   def Comprobar(self, numero):
      try:
         longitud=len(str(numero))
         sumaP=0
         sumaI=0
         for i in range (longitud-1):
            if ((i+1) % 2 == 0) :
               sumaP += int(str(numero)[i])
            else:
               sumaI += int(str(numero)[i])
         if (longitud)==8:
            sumaI=sumaI*3
         elif (longitud)==13:
            sumaP=sumaP*3
         else:
            print(f"El código EAN {numero} no es correcto")

         Total=sumaP+sumaI
         resto=Total%10
         digitoControl=10-resto
         if digitoControl==10:
            digitoControl=0
         if digitoControl==int(str(numero)[longitud-1]):
            print(f"El código EAN {numero} es correcto")
         else:
            print(f"El código EAN {numero} es incorrecto")
      except:
         print(f"Error: {sys.exc_info()}")