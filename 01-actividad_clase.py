# Recorrer Dos Listas Al Mismo Tiempo
animals_type = ['Terrestre', 'Acuatico', 'Aereo']
animals = ['Gato', 'Pez', 'Pajaro']

for category, animal in zip(animals_type, animals):
    print(f'El {animal} Es Un Animal {category}')