# El contenido de una función debe respetar la identación


# Función simple
def hola():
    print('hola')
print('Linea fuera de la función')

hola()

# Función con parámetros
def function_con_parametros(nombre, lugar):
    print('Parámetro ', nombre)
    print(f'Imprimir como variable con llaves {nombre} y estoy en {lugar}')

function_con_parametros('Pedro', 'Ferrol')

# Función que devuelve un valor
def recupera_nombre(nombre):
    return nombre
rec_nombre = recupera_nombre('Jose')
print(f'Nombre recuperado de función {rec_nombre}')