import random

#  константы игры
n = ['Бумага', 'Камень', 'Ножницы']
m = ['Победил', 'Проиграл', 'Ничья']

#  загадывает Алиса
x = random.randint(0, len(n)-1)

#  загадывает Человек
print('Пусть Бумага = 0, Камень = 1, Ножницы = 2')
y = int(input('Введите свой ход: '))

if x == y:  #  если одинаково - Ничья
	r = 2
else:
	if True:  #  тут нужны условия победы Алисы
		r = 1  #  Проиграл
	else:
		r = 0  #  Победил

print(n[x], n[y])
print(m[r])