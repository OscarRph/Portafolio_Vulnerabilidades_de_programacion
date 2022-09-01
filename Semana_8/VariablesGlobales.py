#Funcio n con variables globales dentro de esta
from tkinter import N


def valores():
    #pimero se declaran las variables como globales, para posteriormente ponerle su valor
    global n, N 
    n = 110
    N = 40
    r = n +N
    return r

print(valores())

resta = n - N
print(resta)



