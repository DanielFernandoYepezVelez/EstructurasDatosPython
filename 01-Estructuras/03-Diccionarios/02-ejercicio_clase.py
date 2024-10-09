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