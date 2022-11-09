# 161
# a = range(100)
# for i in a:
#   print(i)

# 162
# a = range(2002, 2051, 4)
# for i in a:
#   print(i)

# 163
# a = range(1, 31)
# for i in a:
#   if i % 3 == 0:
#     print(i)

# 다른 풀이
# a = range(3, 31, 3)
# for i in a:
#   print(i)

# 164
# a = range(0, 100)
# for i in a[::-1]:
#   print(i)

# 다른 풀이
# a = range(100)
# for i in a:
#   print(99 - i)

# 165
# a = range(0, 10)
# for i in a:
#   print(i / 10)

# 166
# a = range(1, 10)
# for i in a:
#   print("3x" + str(i) + " = ", 3 * i)

# 167
# a = range(1, 10)
# for i in a:
#   if i % 2 == 1:
#     print("3x" + str(i) + " = ", 3 * i)


"""오답"""
# 168
# a = range(1, 11)
# b = 0
# for i in a:
#   b = b + i # <---- 0 + 1, 1 + 2, 3 + 3 반복된다
# print("합 :", b)


# 169
# a = 0
# for i in range(1, 11, 2):
#   a = a + i
# print("합 :", a)

# 170
# a = 1
# for i in range(1, 11):
#   a = a * i
# print("답 :", a)