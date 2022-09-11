#Programa que ejemplifica los metodos especiales de python


class FabricaTelefonos():
    #Inet //  Constructor
    def __init__(self, marca, color):
        self.marca = marca
        self.color = color
        print(" El objeto {} ha sido creado".format(self.marca))

    def __str__(self):
        return "El objeto es {}".format(self.marca)

    #Destructor ( se ejecuta al terminar la ejecucion de un codigo) elimina el objeto
    def __del__(self):
                print(" El objeto {} ha sido destruido".format(self.marca))



telefono = FabricaTelefonos( 'Iphone', "Rojo")
print(telefono.marca)
print(telefono.color)
print(telefono)

