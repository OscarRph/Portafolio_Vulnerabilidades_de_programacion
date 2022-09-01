#Escribir una función que calcule el total de una factura tras aplicarle el IVA. La función debe recibir la cantidad sin IVA y el porcentaje de IVA a aplicar, y devolver el total de la factura. 
#Si se invoca la función sin pasarle el porcentaje de IVA, deberá aplicar un 21%.

#Funcion que calcula el total
def total():
    #entrada de datos por consola
    monto = float(input('Ingresa el valor del producto que estas pagando:'))
    iva = int(input('Ingresa el valor del IVA: '))
    #Condicionales para verificar y calcular el IVA
    if iva != 0:
        if iva > 0:
            totalPagar = ((monto*iva)/100) + monto
            return totalPagar
        else:
            return ('El monto de IVA es negativo. No podemos avanzar')
    else:
        totalPagar = (monto *.021) + monto
        return totalPagar

print('El total de su monto es: ', total())