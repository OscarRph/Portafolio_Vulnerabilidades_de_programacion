#Programa que ejecuta diversos metodos de listas
lista = ['Python', 24, 'Oscar', 'xd', 23]

#Modificar un dato
lista[3] = ':v'
print(lista)

#Metodos para eliminar elementos de una lista
lista.pop() #Elimina el ultimo valor de la lista
print(lista)
lista.pop()
lista.remove('Python')#Elimina el dato excato
print(lista)