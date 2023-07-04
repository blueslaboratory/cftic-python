# Day 26 - 04/07/2023
# Librerías Estándar.docx
# Modulo Statistics


import statistics


print('\n*** 1.Medidas de tendencia central ***')
print(statistics.mean([1, 2, 3, 4, 5]))
print(statistics.median([1, 2, 3, 4, 5]))
print(statistics.mode([1, 2, 2, 3, 3, 3, 4, 5])) # valor mas frecuente



print('\n*** 2.Medidas de dispersión ***')
print(statistics.variance([1, 2, 3, 4, 5]))
print(statistics.stdev([1, 2, 3, 4, 5]))



print('\n*** 3.Otras medidas estadisticas ***')
print(min([1, 2, 3, 4, 5]))
print(max([1, 2, 3, 4, 5]))
print(statistics.quantiles([1, 2, 3, 4, 5]))