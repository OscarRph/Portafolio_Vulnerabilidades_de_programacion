class FabricaTelefonos():

    marca = 'Samsung'
    #Recordemos que self es una palabra que nos permite equipar atributos a metodos de instancia
    #(Engloba los atributos a la clase)
    def ElaborarHuawei(self):
        self.marca = "Huawei"

#Objeto
telefono = FabricaTelefonos()
print(telefono.marca)
telefono.ElaborarHuawei()
print(telefono.marca)

#Inet es un metodo que se ejecuta al momento de inicar los objetos, s le conoce como cosntructor
class FabricaTelefonos2():

    def __init__(self, marca, color):
        self.marca = marca
        self.color = color

telefono = FabricaTelefonos2( 'Iphone', "Rojo")
print(telefono.marca)
print(telefono.color)