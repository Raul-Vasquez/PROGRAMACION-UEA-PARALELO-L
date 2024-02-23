#Búsqueda en Arreglo Multidimensional
# declaracion de arreglo 4x4
matriz = [
                [2, 20, 200, 5],       #Fila 1
                [8, 200, 5, 4],     #Fila 2
                [5, 105, 1000, 106],    #Fila 3
                [59, 69, 22, 7]         #Fila 4

      ]
# valor que estamos buscando 1000
valorBuscado = 5

# incializamos variables para rastrear la posicion del valor
filaEncontrada = -1
columnaEncontrada = -1

# recorrer la matriz para encontrar el valor
for fila in range (len(matriz)):
    for columna in range (len(matriz[fila])):
        if matriz [fila][columna]==valorBuscado:
            filaEncontrada = fila
            columnaEncontrada = columna
            break #Detener la busqueda una vez que se encuentra el valor
    if filaEncontrada != -1:
        break # Salir del Bucle exterior si se encuentra el valor

# Verificar si se encontro el valor y mostrar la posicion
if filaEncontrada != -1:
    print (f"Se encontrodo☻ {valorBuscado} en la  fila {filaEncontrada} "
           f"y columna {columnaEncontrada}")
else:
    print (f"{valorBuscado}, no se encuentra en la matriz")