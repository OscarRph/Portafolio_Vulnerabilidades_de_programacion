#Escribir un programa que pregunte al usuario su edad y muestre por pantalla todos los años que ha cumplido (desde 1 hasta su edad).

#Entrada de datos y creacion del iterador
edad = int (input('Digite su edad, para mostrarte tus años: '))
i = 1

#Uso del bucle While 
while i <= edad:
    print('Has cumplido: {} años'.format(i))
    i+=1