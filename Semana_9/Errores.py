#Error del que el usuario ingre string en una variable int

while True:
    try:
        edad = int(input("Ingrese su edad: "))
        print("Tu edad es: ", edad)
        break
    except:
        print('Ingresaste un valor erroneo')
    finally:
        print("haya o no haya error finally siempre se ejecuta")
