def f(x):
    return 2*x*x+3*x+2

k = int(input())
i = 15
while (i > 0 and f(i) > k):
    i -= 1

print(i)
