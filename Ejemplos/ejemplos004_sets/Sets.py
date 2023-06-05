# Day 5 - 05/06/2023

print('\n*** Listas vs Tuplas vs Diccionarios vs Sets ***')
myLista = [69, 5.5, 'hola']
myTupla = (96, 7.7, 'adios')
myDicionario = {'clave0':'valor0', 'clave1':'valor1', 'clave2':'valor2'}
mySet0 = {99, 8.8, 'hasta luego', 7, 9}


mySet1 = {1,2,3,4}
print(mySet1)

mySet1.add(8)
print(mySet1)

# No hay principio ni final en el set:
# mira si estan los valores y si no estan los agrega
mySet1.update([7,8,9])
print(mySet1)

# Remover un valor:
mySet1.remove(3)
mySet1.discard(8)
print(mySet1)

# Coger un valor al AZAR y eliminarlo del conjunto
pop = mySet1.pop()
print(pop)


print('\n*** Sets: Conjuntos ***')
print(mySet0)
print(mySet1)


print('\n*** Sets: union ***')
union = mySet0.union(mySet1)
print(union)


print('\n*** Sets: intersect ***')
intersect = mySet0.intersection(mySet1)
print(intersect)


print('\n*** Sets: difference ***')
difference = mySet0.difference(mySet1)
print(difference)


print('\n*** Sets: symmetric difference ***')
'''
symDif contendra los elementos que estan en mySet0 o en mySet1, 
pero no en ambos conjuntos.
'''
symDif = mySet0.symmetric_difference(mySet1)
print(symDif)