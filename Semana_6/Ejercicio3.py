'''En el siguiente diccionario se encuentran capitales de los paises en el mundo, 
debes realizar un programa que pida un pais al usuario, y muestre la capital de ese pais,
 en dado caso el pais no este en el diccionario, se debe mostrar un mensaje diciendo que ese pais no se encuentra.

{"Guatemala": "Ciudad de Guatemala", "El Salvador": "San Salvador", "Honduras": "Honduras","Nicaragua": "Managua", "Costa Rica": "San Jose",
 "Panama": "Panama", "Argentina": "Buenos Aires", "Colombia": "Bogota", "Venezuela": "Caracas", "España": "Madrid"}
'''

#Creacion del diciconario
D = {"Guatemala": "Ciudad de Guatemala", "EL SALVADOR": "San Salvador", "Honduras": "Honduras","Nicaragua": "Managua", "COSTA RICA": "San Jose", "Panama": "Panama", "Argentina": "Buenos Aires", "Colombia": "Bogota", "Venezuela": "Caracas", "España": "Madrid"}

#Entrada del dato del usuario
pais = input('Ingrese el nombre del pais del que quiere conocer su capital: ')

#Ejecucion del código
if pais.capitalize() in D:
    print(D[pais.capitalize()])
elif pais.upper() in D:
    print(D[pais.upper()])
else:
    print('El pais no se encuentra en el diccionario')