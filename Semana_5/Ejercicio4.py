'''Crear un programa que permita al usuario elegir un candidato por el cual votar. Las posibilidades son: candidato A por el partido rojo, candidato B por el partido verde, candidato C por el partido azul.
Según el candidato elegido (A, B ó C) se le debe imprimir el mensaje “Usted ha votado por el partido [color que corresponda al candidato elegido]”. 
Si el usuario ingresa una opción que no corresponde a ninguno de los candidatos disponibles, indicar “Voto invalido”.
'''
#Entrada del dato
voto = input('Vota por el candidato, ya sea A, B o C: ')

#Ejecucion del ELIF
if voto.upper() == "A":
    print("Usted voto por el partido rojo")
elif voto.upper() == "B":
     print("Usted voto por el partido verde")
elif voto.upper() == "C":
     print("Usted voto por el partido azul")
else:
    print('Voto invalido')