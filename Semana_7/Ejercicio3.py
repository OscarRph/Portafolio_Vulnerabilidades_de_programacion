#Escribir un programa que pida un numero al usuario y muestre las tablas de multiplicar de ese numero

#Creacion de las variables
x = int(input('Inserte un numero, con el fin de saber su tabla de multiplicar: '))
i = 1

#Uso del while
while i <= 10:
    y = x*i
    print ('{} x {} = {}'.format(x,i,y))
    i+=1