'''Escribir un programa que solicite al usuario un vocal en minuscula, y luego una letra en mayúsculas. 
El programa debe convertir la letra en minúscula y la vocal en mayúscula, y al final, 
deben ser concatenadas ambas
'''
#Entrada de las variables
a=input("Ingrese una vocal minuscula: ")
A=input("Ingrese una letra en mayuscula: ")

#Impresion
print(a.swapcase(), A.swapcase())