'''Escribir una tupla que tenga las letras del alfabeto. 
Luego, debes pedir al usuario un número, el que haya ingresado, es la letra que debe imprimir el programa
'''

#CRacion de la tupla que contiene el abecedario dentro
abc = 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'

#Entrada de datos de parte del usuario
n = int(input('Ingrese un numero del 1 al 26: '))

#Impresion de datos mediante un If
if n <= 26 and n>0:
    print ('El numero seleccionado pertenece a la letra: ', abc[n-1])
else:
    print('El numero ingresado no pertenece a ninguna letra del abecedario')