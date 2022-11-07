# 101
# 파이썬에서 True 혹은 False를 갖는 데이터 타입은 무엇인가?
#boolean

# 102
print(3 == 5)
# false

# 103
print(3 < 5)
# true

# 104
x = 4
print(1 < x < 5)
# true

# 105
print ((3 == 3) and (4 != 3)) # != 같지 않다
# true

# 106
# print(3 => 4)
# >= 이렇게 되어야함

# 107
if 4 < 3:
    print("Hello World")
# 출력되지 않는다

# 108
if 4 < 3:
    print("Hello World.")
else:
    print("Hi, there.")
# "Hi, there." 출력

# 109
if True :
    print ("1")
    print ("2")
else :
    print("3")
print("4")
# 만약 true면 1, 2, true가 아니면 3
# 1, 2, 4

# 110
if True :
    if False:
        print("1")
        print("2")
    else:
        print("3")
else :
    print("4")
print("5")
# 만약 true이면 -> (flase이면 3) true가 아니면 4
# 3, 5