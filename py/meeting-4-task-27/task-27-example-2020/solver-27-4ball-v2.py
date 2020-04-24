p = 3  # длина запрещённого участка
n = int(input())
a = [0] * p
for i in range(p):
    a[i] = int(input())

k = 0
n23 = 0
pos = 0
for i in range(p, n):
    if a[pos] % 23 == 0:  # крайний попадёт в левую область
        n23 += 1
    a[pos] = int(input())
    k += (i-p+1) if a[pos] % 23 == 0 else n23
    # pos = 0 if pos + 1 == p else pos + 1  # двигаем позицию в запрещённом массиве
    pos = (pos + 1) % p  # двигаем позицию в запрещённом массиве

print(k)


'''
6
46
2
3
5
4
23
'''
