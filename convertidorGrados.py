def
    convertidor = (grados_centigrados):
    farengei = (9*(grados_centigrados-32))/5
    kelvin = grados_centigrados + 273.15
    return farengei, kelvin

#Solicitud de datos
ingreso_grados= float (input ("Ingrese el valor de los grados: "))

# invocar a la funcion
result_farengei, result_kelvin = convertidor (ingreso_grados)

# imprimir los resultados
print ("Grados Fahrenheit", result_farengei, "Grados Kelvin", result_kelvin)
