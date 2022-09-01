#Funcion en la que asignas solo un valor
def argumento(num):
    return type(num)

#El tipo de dato cambia dependiendo lo que envies
print(argumento(10))
print(argumento(10.36))
print(argumento('xdxd'))

#Funcion en la que no sabes si vas a llegar a enviar mas de un parametro
def argumento2(*num):
    return type(num)

#Los argumentos se almacenan en una tupla
print(argumento2(10,30,50))
