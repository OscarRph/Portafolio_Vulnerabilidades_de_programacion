'''Realizar un programa que haga el proceso de formula general para la resolución de ecuaciones, 
sabiendo que la formula general es la que está en la imagen, el usuario debe ingresar los valores de “a”, “b” y “c”, 
y el programa debe hacer el proceso para que al final muestre el mensaje: “La solución es: <solucion>'''

#Importacion de sqrt, es decir raiz cuadrada
from math import sqrt


#Entrada y creacion de las variables
A = float(input("Ingrese el valor de a\n"))
B = float(input("Ingrese el valor de b\n"))
C = float(input("Ingrese el valor de c\n"))
x1= 0.0
x2= 0.0

#Validacion de que sean numeros reales positivos en la raiz cuadrada
if ((B**2)-4*A*C) < 0:
  print("La solución de la ecuación es con números complejos")
#Procedimiento de la ecuacion
else:
  x1 = (-B+sqrt(B**2-(4*A*C)))/(2*A)
  x2 = (-B-sqrt(B**2-(4*A*C)))/(2*A)
  print("Las soluciones de la ecuación son:")
  print("x1 = ",x1)
  print("x2 = ",x2)