#Muestra si un caracter es vocal o no, pero que el usuario ingrese la letra

letra = input('Ingresa cualquier vocal: ')
if letra.lower() == "a":
    print("Esta vocal es la A")
elif letra.lower() ==  "e":
    print("Vocal es la E")
elif letra.lower() ==  "e":
    print("Vocal es la E")
elif letra.lower() ==  "i":
    print("Vocal es la I")
elif letra.lower() ==  "o":
    print("Vocal es la O")
elif letra.lower() ==  "u":
    print("Vocal es la U")
else:
    print("No es vocal")