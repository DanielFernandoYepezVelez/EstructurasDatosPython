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

# Definir E Inicializar Un Diccionario
fruits = {
    'manzana': 2000,
    'pera': 1500,
    'naranja': 1800,
    'uva': 3000,
    'kiwi': 2500,
    'mango': 2200,
}

# Solicitar El Nombre De Una Fruta Por Consola
name_fruit = input('Ingrese El Nombre De Una Fruta: ').lower()

# Validar Si La Fruta Existe En El Diccionario
if name_fruit in fruits.keys():
    # Solicitar La Cantidad De La Fruta Por Consola
    quantity = int(input('Ingrese La Cantidad Que Desea Comprar: '))

    # Procesos Aritméticos
    price = quantity * fruits[name_fruit]
    
    # Mostrar Información Final Por Consola
    print(f'El Precio Total De La Compra Es: {price}')
else:
    # Mostrar Información Final Por Consola
    print('La Fruta Ingresada No Existe En El Sistema.')