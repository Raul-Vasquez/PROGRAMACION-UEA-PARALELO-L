# Ordenar el arreglo Bidimensional de 3 filas por 3 columnas
arregloBidimensional = [
                        [2,5,8],
                        [4,0,5],
                        [3,4,5]
                    ]
for fila in range (len(arregloBidimensional)):
    for columna in range (len(arregloBidimensional)):
        print (arregloBidimensional [fila][columna])

# metododo sort para una organizacion ascendente
arregloBidimensional.sort()
print("\n__________________________________________________")
print (f"Organizacion Ascendente: \n{arregloBidimensional}")

# metododo sort para una organizacion descendente
arregloBidimensional.sort( reverse = True)
print("\n__________________________________________________")
print (f"Organizacion Descendente: \n{arregloBidimensional}")


