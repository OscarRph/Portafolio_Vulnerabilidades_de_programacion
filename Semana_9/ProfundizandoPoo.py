#Metodo que inserta tuplas y diccionarios en una clase
class FabricaTelefonos():
    def __init__(self , marca , *colores , **modelos):
        self.marca = marca
        self.colores = colores
        self.modelos = modelos

telefono = FabricaTelefonos("Alcatel" , "Negro" , "Azul" , m1 = 500 , m2 = 1000)
print(telefono.marca)
#crear metodo temporal
print(telefono.colores)
print(telefono.modelos)
telefono.memoria = 512
print(telefono.memoria)