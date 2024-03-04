# yarea de la semana 12 sobre temperaturas diarias en diferentes ciudades
tempCiudad = [
    [   # Ciudad del Coca
        [   # Semana 1
            {"day": "Lunes", "temp": 78},
            {"day": "Martes", "temp": 80},
            {"day": "Miércoles", "temp": 82},
            {"day": "Jueves", "temp": 79},
            {"day": "Viernes", "temp": 85},
            {"day": "Sábado", "temp": 88},
            {"day": "Domingo", "temp": 92}
        ],
        [   # Semana 2
            {"day": "Lunes", "temp": 76},
            {"day": "Martes", "temp": 79},
            {"day": "Miércoles", "temp": 83},
            {"day": "Jueves", "temp": 81},
            {"day": "Viernes", "temp": 87},
            {"day": "Sábado", "temp": 89},
            {"day": "Domingo", "temp": 93}
        ],
        [   # Semana 3
            {"day": "Lunes", "temp": 77},
            {"day": "Martes", "temp": 81},
            {"day": "Miércoles", "temp": 85},
            {"day": "Jueves", "temp": 82},
            {"day": "Viernes", "temp": 88},
            {"day": "Sábado", "temp": 91},
            {"day": "Domingo", "temp": 95}
        ],
        [   # Semana 4
            {"day": "Lunes", "temp": 75},
            {"day": "Martes", "temp": 78},
            {"day": "Miércoles", "temp": 80},
            {"day": "Jueves", "temp": 79},
            {"day": "Viernes", "temp": 84},
            {"day": "Sábado", "temp": 87},
            {"day": "Domingo", "temp": 91}
        ]
    ],
    [   # Ciudad de Latacunga
        [   # Semana 1
            {"day": "Lunes", "temp": 62},
            {"day": "Martes", "temp": 64},
            {"day": "Miércoles", "temp": 68},
            {"day": "Jueves", "temp": 70},
            {"day": "Viernes", "temp": 73},
            {"day": "Sábado", "temp": 75},
            {"day": "Domingo", "temp": 79}
        ],
        [   # Semana 2
            {"day": "Lunes", "temp": 63},
            {"day": "Martes", "temp": 66},
            {"day": "Miércoles", "temp": 70},
            {"day": "Jueves", "temp": 72},
            {"day": "Viernes", "temp": 75},
            {"day": "Sábado", "temp": 77},
            {"day": "Domingo", "temp": 81}
        ],
        [   # Semana 3
            {"day": "Lunes", "temp": 61},
            {"day": "Martes", "temp": 65},
            {"day": "Miércoles", "temp": 68},
            {"day": "Jueves", "temp": 70},
            {"day": "Viernes", "temp": 72},
            {"day": "Sábado", "temp": 76},
            {"day": "Domingo", "temp": 80}
        ],
        [   # Semana 4
            {"day": "Lunes", "temp": 64},
            {"day": "Martes", "temp": 67},
            {"day": "Miércoles", "temp": 69},
            {"day": "Jueves", "temp": 71},
            {"day": "Viernes", "temp": 74},
            {"day": "Sábado", "temp": 77},
            {"day": "Domingo", "temp": 80}
        ]
    ],
    [   # Ciudad del Tena
        [   # Semana 1
            {"day": "Lunes", "temp": 90},
            {"day": "Martes", "temp": 92},
            {"day": "Miércoles", "temp": 94},
            {"day": "Jueves", "temp": 91},
            {"day": "Viernes", "temp": 88},
            {"day": "Sábado", "temp": 85},
            {"day": "Domingo", "temp": 82}
        ],
        [   # Semana 2
            {"day": "Lunes", "temp": 89},
            {"day": "Martes", "temp": 91},
            {"day": "Miércoles", "temp": 93},
            {"day": "Jueves", "temp": 90},
            {"day": "Viernes", "temp": 87},
            {"day": "Sábado", "temp": 84},
            {"day": "Domingo", "temp": 81}
        ],
        [   # Semana 3
            {"day": "Lunes", "temp": 91},
            {"day": "Martes", "temp": 93},
            {"day": "Miércoles", "temp": 95},
            {"day": "Jueves", "temp": 92},
            {"day": "Viernes", "temp": 89},
            {"day": "Sábado", "temp": 86},
            {"day": "Domingo", "temp": 83}
        ],
        [   # Semana 4
            {"day": "Lunes", "temp": 88},
            {"day": "Martes", "temp": 90},
            {"day": "Miércoles", "temp": 92},
            {"day": "Jueves", "temp": 89},
            {"day": "Viernes", "temp": 86},
            {"day": "Sábado", "temp": 83},
            {"day": "Domingo", "temp": 80}
        ]
    ]
]
# Acceso a los valores de cada ciudad y semana
for fila in range (len(tempCiudad)):
    for columna in range (len(tempCiudad[fila])):
        for pag in range (len(tempCiudad[fila][columna])):
            print ("Fila: ", fila, "Columna: ", columna, "Pagina: ", pag,"--->", tempCiudad[fila][columna][pag])

# mostrar los valores del arreglo 3D
print ("Temperaturas Ciudad del Coca")
print (tempCiudad[0][0][0]['day'])  # indice 0
print (tempCiudad[0][0][0]['temp'])  # indice 1

print (tempCiudad[0][0][1]['day'])  # indice 0
print (tempCiudad[0][0][1]['temp'])  # indice 1

print (tempCiudad[0][0][2]['day'])  # indice 0
print (tempCiudad[0][0][2]['temp'])  # indice 1

print (tempCiudad[0][0][3]['day'])  # indice 0
print (tempCiudad[0][0][3]['temp'])  # indice 1

print (tempCiudad[0][0][4]['day'])  # indice 0
print (tempCiudad[0][0][4]['temp'])  # indice 1

print (tempCiudad[0][0][5]['day'])  # indice 0
print (tempCiudad[0][0][5]['temp'])  # indice 1

print (tempCiudad[0][0][6]['day'])  # indice 0
print (tempCiudad[0][0][6]['temp'])  # indice 1

print("Ciudad de Latacunga")
print (tempCiudad[1][0][0]['day'])  # indice 0
print (tempCiudad[1][0][0]['temp'])  # indice 1

print (tempCiudad[1][0][1]['day'])  # indice 0
print (tempCiudad[1][0][1]['temp'])  # indice 1

print (tempCiudad[1][0][2]['day'])  # indice 0
print (tempCiudad[0][0][2]['temp'])  # indice 1

print (tempCiudad[1][0][3]['day'])  # indice 0
print (tempCiudad[1][0][3]['temp'])  # indice 1

print (tempCiudad[1][0][4]['day'])  # indice 0
print (tempCiudad[1][0][4]['temp'])  # indice 1

print (tempCiudad[1][0][5]['day'])  # indice 0
print (tempCiudad[1][0][5]['temp'])  # indice 1

print (tempCiudad[1][0][6]['day'])  # indice 0
print (tempCiudad[1][0][6]['temp'])  # indice 1