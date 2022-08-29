#Sintaxis de una tupla
tupla = (1, 2, 3, 4, 5)
tupla2 = 6, 7, 8, 9, 10

print(tupla)
print(type(tupla))
print(tupla2)
print(type(tupla2))

#impresion de un dato especifico dentro de una tupla
print(tupla[3])
#Debanado
print(tupla[0:3])
#Suma de dos tuplas
print(tupla+tupla2)
#Demostracion que los datos de una tupla son inmutables
tupla[2] = 20
print (tupla)