days_week = ('Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes', 'Sabado', 'Domingo')

# Métodos De La Estructura
print(type(days_week))
print(days_week[2])
print(days_week.index('Jueves'))
print(days_week.count('Viernes'))

# Convertir Tupla A Lista
days_week = list(days_week)
print(type(days_week))
del days_week