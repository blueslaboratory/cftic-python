
producto = input('Nombre del producto: ')
precioUnitario = float(input('Precio unitario: '))
unidades = int(input('Unidades: '))
costeTotal = precioUnitario * unidades

cadenaFinal = f'Producto: {producto}\n'
cadenaFinal += f'Precio unitario con 0s: {precioUnitario:06.2f}\n'
cadenaFinal += f'Precio unitario: {precioUnitario:6.2f}\n'
cadenaFinal += f'Unidades con 0s: {unidades:03d}\n'
cadenaFinal += f'Unidades: {unidades:3d}\n'
cadenaFinal += f'Coste total con 0s: {costeTotal:08.2f}\n'
cadenaFinal += f'Coste total: {costeTotal:8.2f}'

print(cadenaFinal)