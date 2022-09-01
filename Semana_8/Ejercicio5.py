#Crear un programa que tenga dos funciones, una que contenga el area de un cuadrado con argumentos de base y altura; y la otra el area de un circulo con argumento de radio
from math import pi

#Funcion del cuadrado
def areaCuadrado(base, altura):
    return base * altura

print(areaCuadrado(10,10))
#Funcion del circulo
def areaCirculo(radio):
    return radio**2*pi

print(areaCirculo(5))