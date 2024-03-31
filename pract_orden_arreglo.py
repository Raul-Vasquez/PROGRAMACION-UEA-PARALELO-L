# algoritimo que permite ordenar los arreglos de matriz de 3*3
practica = [
            [8,5,69],
            [20,7,6],
            [1,9,2]
        ]
# Acceso a las logitud del arreglo Bidimensional
for fila in range (len(practica)):
    for m in range (len(practica)):
        for columna in range (len(practica)):
            if columna < len (practica[fila]) -1:
                if practica [fila][columna] > practica [fila][columna+1]:
                    variable_temporal = practica[fila][columna]
                    practica [fila][columna] = practica [fila][columna+1]
                    practica [fila][columna+1]=variable_temporal

# Imprimir los rsultados ordenados
print (practica)

