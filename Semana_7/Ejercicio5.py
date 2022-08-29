'''Imprimir por pantalla los numeros del 1 al 10,
luego, pedir al usuario dos numeros y mostrar el rango de numeros entre ambas cifras'''


#Impresion de pantalla del 1 al 10
for i in range (1, 11):
    print (i)

#Entrada del numero por parte del usuario
n = int(input('Ingresa la primera cifra: '))
N = int(input('Ingresa la primera cifra: '))

for i in range (n, N+1):
    print(i)