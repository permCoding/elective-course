n = int(input())
a = [0] * n
for i in range(n):
    a[i] = int(input())

k = 0
for i in range(n - 7):
    for j in range(i + 7, n):
        if a[i] + a[j] > k:
            k = a[i] + a[j]

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
