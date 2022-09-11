#Excepciones especiales de python

#Ejemplo de excepcion conocida (division entre 0)
while True:
    try:
        Num=int(input("Ingresa un numero: "))
        resultado = 100 / Num
        break
    except ZeroDivisionError:
        print('No se puede dividir entre 0')

#Ejemplo de recibir un tipo de dato diferente al especificado
while True:
    try:
        edad = int(input("Ingrese su edad: "))
        print("Tu edad es: ", edad)
        break
    except ValueError:
        print('Has colocado un valor erroneo')

#Ejemplo de cancelar la ejecucion con entradas de teclado (Ctrl + C)
while True:
    try:
        edad = int(input("Ingrese su edad: "))
        print("Tu edad es: ", edad)
        break
    except KeyboardInterrupt:
        print('\nHas cancelado la ejecucion')