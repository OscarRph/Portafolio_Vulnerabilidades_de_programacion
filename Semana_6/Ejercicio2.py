'''Escribe una lista que tenga los números de 1 al 10. Luego, debes hacer que los datos que están en las posiciones
 4, 7 y 9 sean multiplicados por 2; por último, mostrar la lista nueva con los nuevos datos'''

#Creacion de la lista
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print('La lista original es: \n', lista)

#Ejecucion del ejercicio
lista[4] *=2
lista[7] *=2
lista[9] *=2

#Impresion final
print('La nueva lista es: \n', lista)