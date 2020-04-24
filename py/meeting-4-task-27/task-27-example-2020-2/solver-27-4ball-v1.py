p = 7  # длина запрещённого участка
n = int(input())
a = [0] * p
for i in range(p):
    a[i] = int(input())

k = 0
leftMax = 0
for i in range(p, n):
    if a[0] > leftMax:  # крайний попадёт в левую область
        leftMax = a[0]
    r = int(input())
    if r + leftMax > k:
        k = r + leftMax
    for j in range(p-1):  # двигаем запрещённый массив
        a[j] = a[j + 1]
    a[p-1] = r

print(k)



'''
10
1
2
3
4
5
6
7
8
9
10
'''
