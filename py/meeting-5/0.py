a = []
for i in range(0, 11):
    tmp = []
    for j in range(0, 11):
        tmp.append( 0 )
    a.append( tmp )

for i in range(1, 11):
    for k in range(1, 11):
        if i == k:
            a[i][k] = 1
        else:
            a[i][k] = -1

acc = 0
for i in range(1, 11):
    for k in range(1, 11):
        print(a[i][k], '  ', end='')
        acc += a[i][k]
    print()

print(acc)