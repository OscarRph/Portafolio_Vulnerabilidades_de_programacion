'''En la siguiente lista, debes hacer un programa que muestre los valores al usuario,
 a su vez, debe pedir dos datos y esos que sean ingresados deben ser 
 sustituidos en el primer y segundo lugar:

[20, 50, "Curso", 'Python', 3.14]
'''
#Creacion de la lista
lista = [20, 50, 'Python', 3.14]

#Impresion de la lista original
print('La lista original es: ', lista, '\nModifiquela: ')

#Modificacion de los primeros dos elementos de la lista
lista[0] = int(input('Ingrese un nuevo numero: '))
lista[1] = int(input('Ingrese otro nuevo numero: '))

#Impresion final
print('La nueva lista es: ', lista)
