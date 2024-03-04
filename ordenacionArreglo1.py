# Ordenar el arreglo Bidimensional de 3 filas por 3 columnas
arregloBidimensional = [
                        [2,8,5],
                        [4,0,5],
                        [3,4,5]
                    ]
for fila in range (len(arregloBidimensional)):
    for columna in range (len(arregloBidimensional[fila])):
        if columna == len (arregloBidimensional[fila])-1:
            print (arregloBidimensional[fila][columna])

        else:

            if arregloBidimensional [fila][columna] > arregloBidimensional [fila][columna +1]:
                               # [0]     [0] >                           [0]     [1]
                                    #2                                        8
                               # [0]     [1] >                           [0]     [2]
                                   # 8                                        5
                varTemporal = arregloBidimensional [fila][columna]
                arregloBidimensional [fila][columna] =  arregloBidimensional [fila][columna + 1]
            # if arregloBidimensional [fila][columna+1]:

                arregloBidimensional [fila][columna +1] = varTemporal
                print (arregloBidimensional [fila][columna])
                print (arregloBidimensional [fila][columna+1])
            else:
                print (arregloBidimensional [fila][columna])






