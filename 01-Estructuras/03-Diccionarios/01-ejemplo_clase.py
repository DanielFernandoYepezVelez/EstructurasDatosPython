personal_information_one = {
    'name': 'Daniel',
    'last_name':'Yepez',
    'age':31,
    'gender':'Masculino'
}

print(type(personal_information_one))

personal_information_two = dict(
    name = 'Daniel',
    last_anme = 'Yepez',
    age = 31,
    gender = 'Masculino'
)

print(type(personal_information_two))

# Acceder personal information
# print(personal_information_one.get('name'))
print(personal_information_one['name'])
print(personal_information_one['age'])
personal_information_one['age'] = 45
personal_information_one['birth_date'] = '07/01/28'

print(personal_information_one['birth_date'])

# pop()
# popitem()
# del, clear
# keys(), values(), items(),
print('\n===== KEYS =====')
for key in personal_information_one.keys():
    print(key)

print('\n======= VALUES =======')
for key in personal_information_one.values():
    print(key)

print('\n======= ITEMS =======')
for key in personal_information_one.items():
    print(key)