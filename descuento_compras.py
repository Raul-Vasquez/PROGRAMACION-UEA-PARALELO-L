#Trabajao de la semana  14
# calcule el descuento en compras en función del monto total de la compra y mostrar el monto final a pagar
# Parámetros y Retorno de Valores en Funciones
def calcularDescuento (montoTotal, xcentajeDescuento=10):
    descuento =  montoTotal * (xcentajeDescuento/100)
    return descuento

# Ejemplo de como se ejecuta la funcion
print ("Objeto 1 descuento del 10%")
objeto1= 100
descuento1= calcularDescuento (objeto1)
montoFinal= objeto1 - descuento1
print ('Monto de descuento: ', descuento1)
print ('Valor Total a pagar: ', montoFinal)

# Ejemplo de como se ejecuta la funcion
print ("Objeto 12 descuento del 20%")
articulo1= 200
descuento2= calcularDescuento (articulo1)
montoFinal1= articulo1-descuento2
print ('Monto Descontado: ', descuento2)
print('Valor Total a pagar: ', montoFinal1)

