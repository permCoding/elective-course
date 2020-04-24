p = 3 # длина запрещённого участка
n = int(input())
a = [0] * p
for i in range(p):
    a[i] = int(input())

k = 0
n23 = 0
for i in range(p, n):
    if a[0] % 23 == 0:  # крайний попадёт в левую область
        n23 += 1
    r = int(input())
    if r % 23 == 0:
        k += (i-p+1)
    else:
        k += n23
    for j in range(p-1):  # двигаем запрещённый массив
        a[j] = a[j + 1]
    a[p-1] = r

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
