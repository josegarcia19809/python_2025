nums = [1, 2, 3, 4, 5]
doubles = list(map(lambda n: n * 2, nums))
print(doubles)  # [2, 4, 6, 8, 10]

people = ["Christina", "Rox", "Annabel"]
print(list(map(lambda person: person.upper(), people)))  # ['CHRISTINA', 'ROX', 'ANNABEL']

personas = [
    {"firstname": "Juan", "lastname": "Pérez"},
    {"firstname": "María", "lastname": "Gómez"},
    {"firstname": "Carlos", "lastname": "Rodríguez"},
    {"firstname": "Ana", "lastname": "Fernández"},
    {"firstname": "Luis", "lastname": "Martínez"}
]

print(list(map(lambda person: person["firstname"], personas)))


# ['Juan', 'María', 'Carlos', 'Ana', 'Luis']


# Sin usar lambdas
def double2(num): return num * 2


print(list(map(double2, nums)))  # [2, 4, 6, 8, 10]
