# Day 26 - 04/07/2023
# Librerías Estándar.docx
# Modulo Datetime

import datetime
from datetime import time



print('\n*** 1.Clase datetime ***')

fecha_actual = datetime.datetime.now()
print(fecha_actual)

# Crear un objeto datetime para el 15 de marzo de 2022 a las 14:30:00
fecha_hora = datetime.datetime(2022, 3, 15, 14, 30, 0)
# Imprimir el objeto datetime
print(fecha_hora)

# Formatear la fecha objeto en formato "YYYY-MM-DD"
fecha_formateada = fecha_hora.strftime("%Y-%m-%d")

# Imprimir la fecha formateada
print(fecha_formateada)

# Crear una nueva instancia de datetime reemplazando el año
nueva_fecha = fecha_hora.replace(year=2030)

# Imprimir la nueva fecha
print(nueva_fecha)



print('\n*** 2.Clase date ***')

print(datetime.date.today())

# Crear un objeto date para el 14 de febrero de 2022
fecha_dia = datetime.date(2022, 2, 14)

# Formatear la fecha en formato "YYYY-MM-DD"
fecha_formateada = fecha_dia.strftime("%Y-%m-%d")

# Imprimir la fecha formateada
print(fecha_formateada)

# Crear una nueva instancia de date reemplazando el año
nueva_fecha = fecha_dia.replace(month=12)

# Imprimir la nueva fecha
print(nueva_fecha)



print('\n*** 3.Clase time ***')

# Crear un objeto time para las 14:30:00
hora = time(14, 30, 0)

# Formatear la hora en formato "HH:MM:SS"
hora_formateada = hora.strftime("%H:%M:%S")

# Imprimir la hora formateada
print(hora_formateada)

# Crear una nueva instancia de time reemplazando los minutos
nueva_hora = hora.replace(minute=49)

# Imprimir la nueva hora
print(nueva_hora)