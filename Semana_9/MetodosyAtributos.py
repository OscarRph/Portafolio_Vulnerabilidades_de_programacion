#programa que ejemplifica el uso de metodos y atributos

#Clase ejemplificando una fabrica de telefonos
class FabricaTelefonos():
    #Atributos de un telefono
    marca = 'Huawei'
    color = 'Negro'
    RAM = 32
    almacenamiento = 512

    #Metodo de instancia
    def llamar(self, mensaje):
        return mensaje

    def escucharMusica(self):
        print('Estas escuchando musica')

#Objeto
telefono = FabricaTelefonos()
#Los atributos de la clase se le heredan al objeto
print(telefono.marca)
print(telefono.color)
print(telefono.RAM)
print(telefono.almacenamiento)

#Acceder al metodo desdde el objeto
print(telefono.llamar("Hola, Con quien hablo?"))
telefono.escucharMusica()