'''Con el siguiente diccionario, debes crear un programa que pregunte al usuario por un número; el programa debe imprimir el jugador al que hace referencia ese número

{

    1 : "Casillas", 15 : "Ramos",

    3 : "Pique", 5 : "Puyol",

    11 : "Capdevila", 14 : "Xabi Alonso",

    16 : "Busquets", 8 : "Xavi Hernandez",

    18 : "Pedrito", 6 : "Iniesta",

    7 : "Villa"

}

'''

#Creacion del diccionario
jugadores = { 1 : 'Casillas', 3 : 'Pique', 5 : 'Puyol', 6 : 'Iniesta', 7 : 'Villa', 11 : 'Capdevila', 14 : 'Xabi Alonso', 16 : 'Busquets', 18 : 'Pedrito'}

num = int(input('Ingrese el numero para saber a que jugador le pertenece: '))

if num in jugadores:
    print(jugadores[num])
else:
    print('El numero que digitaste no esta en la lista')