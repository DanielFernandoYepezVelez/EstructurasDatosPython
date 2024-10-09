"""
    Solicitar Un Número Por Teclado
    Y crear un diccionario, cuyas claves
    sean desde 1 hasta el numero ingresado
    y los valores sean el cubo de las claves.
    Mostrar claves y su valor correspondiente. 
"""
"""
# Solicitar un número al usuario
numero = int(input("Ingresa un número: "))

# Crear un diccionario con claves desde 1 hasta el número ingresado
diccionario = {
    i: i ** 3 for i in range(1, numero + 1)
}

# Mostrar claves y sus valores correspondientes
for clave, valor in diccionario.items():
    print(f"{clave}: {valor}")
"""
# Definir E Iniciarlizar Un Diccionario
number_dict = {}

# Solicitar un número al usuario
number = int(input("Ingresa un número: "))

# Estructura Cíclica Para O For
for i in range(1, number + 1, 1):
    number_dict[i] = i ** 3

# Mostrar claves y sus valores correspondientes
for clave, valor in number_dict.items():
    print(f"{clave}: {valor}")