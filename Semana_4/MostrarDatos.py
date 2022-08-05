#Entrada por teclado
#Entrada Strings
nombre = input('Ingresa tu nombre: ')
#Entrada enteros
edad = int(input("Ingresa tu edad: "))

#Mostrar datos "normal"
print(nombre)
print(edad)

#Impresion de datos con concatenacion
print("Hola", nombre, "tienes ", edad, "años")

#Impresion de datos con format
print("Hola {}, tienes {} años".format(nombre,edad))