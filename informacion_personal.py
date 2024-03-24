# Crear un diccionario con información ficticia
informacion_personal = {
    "nombre": "John McClane",
    "edad": 35,
    "ciudad": "Buenos Aires",

}

# Acceder y modificar el valor de la clave "ciudad"
informacion_personal["ciudad"] = "Buenos Aires"

# Agregar una nueva clave-valor al diccionario
informacion_personal["profesion"] = "hackers"

# Verificar si la clave "telefono" existe y agregarla si no
if "telefono" not in informacion_personal:
    informacion_personal["telefono"] = "+36412548925"

# Eliminar la clave "edad" del diccionario
del informacion_personal["edad"]

# Imprimir el diccionario final
print(informacion_personal)