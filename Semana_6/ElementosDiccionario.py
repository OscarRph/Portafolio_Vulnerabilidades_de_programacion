#Creacion del diccionario
diccionario = {'Nombre' : "Oscar", 'Apellido' : "Perez", 'Estatura' : 1.70}

#Impresion de solo las llaves
print(diccionario.keys())
#Impresion de solo los valores
print(diccionario.values())

#Impresion de una unica llave
print(diccionario['Estatura'])

#Agregar una nueva clave y llave
diccionario['Peso'] = 80
print(diccionario)

#Modificar un valor
diccionario["Nombre"] = 'Artek'
print(diccionario)