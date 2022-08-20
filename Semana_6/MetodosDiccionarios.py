#Creacion de un diccionario
diccionario = {1 : 2, 2 : 3, 3 : 4}
diccionario2 = {1 : 2, 2 : 3, 3 : 4}

print(diccionario)

#Metodo para eliminar un parametro
diccionario.pop(3)
print(diccionario)

#Metodo para que devuelva un valor
print(diccionario.get(2))

#Metodo para limpiar el diccionario
diccionario.clear()
print(diccionario)

#Metodo para agregar valores
diccionario.setdefault(4 , 5)
print(diccionario)

#Metodo para actuallizar un diccionario a partir de otro, como si fuese una combinacion
diccionario.update(diccionario2)
print(diccionario)

#Metodo para hacer una copia del diccionario
diccionario.copy()