#Diferencia entre conjunto y lista
print('Diferencia entre lista y conjuntos\n')
conjunto = {1, 1, 2, 3, 4, 5}
lista = [1, 2, 3, 4, 4]

print (lista)
print(conjunto)
#Como se ve, el conjunto no acepta datos repetidos, por lo que no los imprime

print('')

print('Metodos\n')
#Metodos con Conjuntos
conjunto2 = {1, 2, 3, 4, 5}
#Añadir datos
conjunto2.add(20)
print (conjunto2)
#Eliminar datos
conjunto2.remove(1)
conjunto2.discard(20)
print (conjunto2)
#Elimnar ddatos con pop,(elimina el ultimo de la pila)
conjunto2.pop()
print(conjunto2)
#Añadir elementos iterables
conjunto2.update([7, 8, 9])
#Dejar al conjunto vacio
conjunto.clear()
print(conjunto2)