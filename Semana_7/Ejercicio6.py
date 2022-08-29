#Pedir al usuario que ingrese 2 numeros, después, se debe mostrar el rango de esos 2 números, pero, solo imprimiendo los números que sean impares



#Entrada del numero por parte del usuario
n = int(input('Ingresa la primera cifra: '))
N = int(input('Ingresa la primera cifra: '))

#Ejecucion del ejercicio
for i in range (n, N+1):
    if i%2==0:
        continue
    else:
       print(i)