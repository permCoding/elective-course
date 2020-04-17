import random

n = ['Бумага', 'Камень', 'Ножницы']

x = random.randint(0, 2)
s = n[x]

print(s)

#  или так:

print(['Бумага', 'Камень', 'Ножницы'][random.randint(0, 2)])
