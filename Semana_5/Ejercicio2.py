#Escribir un programa que, dado un número entero, muestre su valor absoluto. 
# Nota: para los números positivos su valor absoluto es igual al número (el valor absoluto de 52 es 52),
# mientras que, para los negativos, su valor absoluto es el número multiplicado por -1 (el valor absoluto de -52 es 52).

#Creacion de variables
num = int(input("Ingresa un numero: "))

#Ejecución del elif
if num > 0:
    print("El valor absoluto de {} ingresado es: {} ".format(num, num))
elif num < 0:
    print("El valor absoluto de {} ingresado es: {} ".format(num, abs(num)))
else:
    print("El numero ingresado es: 0")
