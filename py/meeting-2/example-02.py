# x = int(input())
# y = int(input())

# # print(ord(x))
# # print(ord(y))

# if x > y:
# 	print(x)
# else:
# 	print(y)


# z = 37
# print(9<z<100)
# print('+++' if z % 11 == 0 else '---')

# x = input('Введите двузначное число:')

# 1
# if len(x) == 2:
# 	result = int(x[0]) + int(x[1])
# else:
# 	result = 'сам дурак'

# 2
# if len(x) == 2:
# 	c1 = ord(x[0]) - 48
# 	c2 = ord(x[1]) - 48
# 	result = c1 + c2
# else:
# 	result = 'сам дурак'

# 3
# x = int(x)
# result = x//10 + x%10

# // div
# %  mod

# print(result)


x = '132 34 5555' # input()
arr = x.split(' ')
a = int(arr[0])
b = int(arr[1])
mn = a if a < b else b
mx = a if a > b else b
print(mn, mx)
print(mn, mx, sep='')
