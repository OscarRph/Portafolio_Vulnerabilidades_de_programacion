'''Se desea tener un algoritmo que permita determinar y mostrar el promedio que ha obtenido un alumno en un determinado curso, conociendo las notas de: tres prácticas, el examen parcial y el examen final.

Considere:

PP = ( P1 + P2 +P3 ) / 3 
PROM = ( PP + 2*EP + 3*EF ) / 6

Donde: P1, P2, P3 : Practicas

PP: promedio de práctica

PROM: promedio

EP: examen parcial

EF: examen final
'''
#Entrada de datos
P1 = float(input("Ingrese calificacion de practica 1\n"))
P2 = float(input("Ingrese calificacion de practica 2\n"))
P3 = float(input("Ingrese calificacion de practica 3\n"))

eP= float(input("Ingrese calificacion del examen parcial\n"))
eF= float(input("Ingrese calificacion del examen final\n"))

#Promedio de practicas
pP = (P1+P2+P3)/3

#Premedio final
Prom = (pP+2*eP+3*eF)/6

#Impresion del promedio final
print("Su promedio final es de: ", Prom)
