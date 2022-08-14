#Escribe un programa que pida dos palabras y diga si riman o no.
#Si coinciden las tres últimas letras tiene que decir que riman. Si coinciden sólo las dos últimas tiene que decir que riman un poco y si no, que no riman.

#Variables que ingresa el usuario por teclado
k =  input('Ingresa una palabra: ')
l = input('Ingresa otra palabra: ')

#Ejecución ELIF
if k[-3:]== l[-3:]:
    print ('Ambas palabras riman')
elif k[-2:]== l[-2:]:
     print ('Ambas palabras riman poco ')
else:
     print ('Ambas palabras no riman')