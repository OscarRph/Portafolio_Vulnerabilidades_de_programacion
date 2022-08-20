#Programa que ejecuta diversos metodos de listas
lista = [1, 2, 5, 3, 4, 5]
lista2 = [2, 4, 5, 3, 1, 6]

#Metodo que cuenta cuantas veces aparece un dato en la lista
print(lista.count(5))

#Metodo que busca un dato y te retorna en que lugar esta
print(lista.index(4))

#Metodo que ordena la lista  de forma ascendente
lista2.sort()
print(lista2)
#Metodo que ordena la lista  de forma descendente
lista2.reverse()
print(lista2)