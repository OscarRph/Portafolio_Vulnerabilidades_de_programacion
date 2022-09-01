#Crear un programa que tenga una lista, luego crear una funcion con la cual se van a pedir numeros al usuario para agregar a la lista. Debes crear una segunda funcion en donde se ordenen los numeros pares e impares dentro de dos listas nuevas

#Creacion  global de la lista
lista=[1, 20, 50, 67, 3, 9, 40]
#Creacion de las listas par e impar
par = []
impar = []

def ori():
    print(lista)

#Funcion donde el usuario agrega numeros a la lista
def ad():
    a = int(input('¿Cuantos números quieres agregar: '))
    #Ciclo for, para llenar la lista
    for i in range(a):
        n = int(input('Ingrese un numero positivo: '))
        #Condicional para validar que los numeros ingresados sean positivos
        if n > 0: 
            lista.append(n)
        else:
            print('El numero ingresado no es positivo')
    lista.sort()

#Funcion donde se crean dos listas, la de los numeros pares e impares
def listas():
    #Ciclo for para llenar las listas dependiendo si son par o impar
    for i in lista:
        #Condicional que se encargara de dividir los numeros impares de los pares
        if i%2==0:
           par.append(i)
        else:
            impar.append(i) 

#Inicializacion de las funciones e impresiones
print('La lista original es: ')
ori()
ad()
print('La nueva lista es: ',lista)
listas()
print('La lista par es: ', par)
print('La lista impar es: ', impar)
#Impresiones

