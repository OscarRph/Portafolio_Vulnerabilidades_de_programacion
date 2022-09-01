#Crear una funcion que pida dos numeros. Si el primero es mayor al segundo, el programa debe retornar el valor 1; si el segundo es mayor al primero, debe retornar -1; si ambos son iguales, debe retornar 0

#Funcion con retorno
def xd():
    n = int(input('Ingrese un numero: '))
    N = int(input('Ingrese otro numero: '))

    if n > N:
        return 1
    elif N > n:
        return -1
    else: 
        return 0
    
print(xd())