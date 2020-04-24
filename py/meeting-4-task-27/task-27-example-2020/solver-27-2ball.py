n = int(input())
a = [0] * n
for i in range(n):
    a[i] = int(input())

k = 0
for i in range(n - 3):
    for j in range(i + 3, n):
        if a[i] * a[j] % 23 == 0:
            print(a[i], a[j])
            k += 1

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
