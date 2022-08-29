'''Escribir una tupla con los meses del año, 
luego, pide al usuario un numero, el que haya ingresado, 
es el mes que debe mostrar en la tupla
'''

#Creacion de la tupla
Meses = 'Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre'

#Entrada de datos de parte del usuario
n = int(input('Ingrese un numero del 1 al 12: '))

#Impresion de datos mediante un If
if n <= 12 and n>0:
    print ('El numero seleccionado pertenece al mes: ', Meses[n-1])
else:
    print('El numero ingresado no pertenece a ningun mes')
