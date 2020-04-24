x = int(input())

L = x - 21
M = x + 12
while L != M:
    if L > M:
        L = L - M
    else:
        M = M - L

print(x, M)