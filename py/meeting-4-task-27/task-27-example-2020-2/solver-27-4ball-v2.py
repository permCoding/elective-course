p = 7  # длина запрещённого участка
n = int(input())
a = [0] * p
for i in range(p):
    a[i] = int(input())

k = 0
leftMax = 0
pos = 0
for i in range(p, n):
    if a[pos] > leftMax:  # крайний попадёт в левую область
        leftMax = a[pos]
    r = int(input())
    if r + leftMax > k:
        k = r + leftMax
    pos = (pos + 1) % p

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
