print('\n *** 1. Operadores aritmeticos ***')

a = 10
b = 3

# Suma
resultado = a + b  # 13

# Resta
resultado = a - b  # 7

# Multiplicación
resultado = a * b  # 30

# División
resultado = a / b  # 3.33333

# División entera (cociente)
resultado = a // b  # 3

# Módulo (resto)
resultado = a % b  # 1

# Potencia
resultado = a ** b  # 1000




print('\n *** 2. Operadores de Comparacion ***')
a = 5
b = 10

# Igual a
resultado = a == b  # False

# Diferente de
resultado = a != b  # True

# Mayor que
resultado = a > b  # False

# Menor que
resultado = a < b  # True

# Mayor o igual que
resultado = a >= b  # False

# Menor o igual que
resultado = a <= b  # True




print('\n *** 3. Operadores de asignación ***')

a = 5

# Asignación simple
b = a  # b = 5

# Asignación con operación
a += 3  # a = a + 3 --> a = 8

# Asignación con operación de resta
a -= 2  # a = a - 2 --> a = 6

# Asignación con operación de multiplicación
a *= 4  # a = a * 4 --> a = 24

# Asignación con operación de división
a /= 6  # a = a / 6 --> a = 4.0

# Asignación con operación de módulo
a %= 3  # a = a % 3 --> a = 1.0

# Asignación con operación de potencia
a **= 2  # a = a ** 2 --> a = 1.0




print('\n *** 4. Operadores Logicos ***')

a = True
b = False

# Operador AND
resultado = a and b  # False

# Operador OR
resultado = a or b  # True

# Operador NOT
resultado = not a  # False




print('\n *** 5.Operadores de Identidad ***')

a = [1, 2, 3]
b = [1, 2, 3]
c = a

# Operador is
resultado = a is b  # False

# Operador is not
resultado = a is not b  # True

# Comparación de identidad con el mismo objeto
resultado = a is c  # True




print('\n *** 6.Operadores de Pertenencia ***')

lista = [1, 2, 3]
diccionario = {'a': 1, 'b': 2}
cadena = "Hola"

# Operador in
resultado = 2 in lista  # True

# Operador not in
resultado = 'c' not in diccionario  # True

# Operador in con cadena
resultado = 'a' in cadena  # True