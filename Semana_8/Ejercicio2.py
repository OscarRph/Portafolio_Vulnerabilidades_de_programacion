#Escribir una función que reciba un número entero positivo y devuelva su factorial.

#Funcion que saca el factorail de un numero
def factoria():
    
    #Creacion de las variables
    f = 1
    a=  False

    #Ciclo while para validar que sea un numero positivo
    while a == False:
        n = int(input('Ingrese el numero que desea saber su factorial: '))

        if n > 0:
            a = True
        else:
            print('El numero ingresado es negativo, por favor ingrese otro numero')
    #ciclo for para hacer el factorial
    for i in range(n+1):
        if i == 0:
            continue
        else:
            f*=i
    print ('El factorial de {} es: {}'.format(n,f))

factoria()