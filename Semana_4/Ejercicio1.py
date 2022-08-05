'''Crear un programa, que tenga una variable con la cadena “Te quiero solo como amigo”, y muestre la siguiente información:

• Imprima los dos primeros caracteres.

• Imprima los tres últimos caracteres.

• Imprima dicha cadena cada dos caracteres. Ej.: Si la cadena fuera “recta” debería imprimir rca

• Dicha cadena en sentido inverso. Ej.: Si la cadena fuera hola mundo! debe imprimir !odnum aloh

• Imprima la cadena en un sentido y en sentido inverso. Ej: Si la cadena es “reflejo” imprime reflejoojelfer.
'''

#Creacion de la cadena
k = "Te quiero solo como amigo"

#Respuestas

print("Respuesta 1.- ")
print(k[0:2])
print("Respuesta 2.- ")
print(k[-3:])
print("Respuesta 3.- ")
print(k[::2])
print("Respuesta 4.- ")
print(k[::-1])
print("Respuesta 5.- ")
print(k+k[::-1])