# 변수 (Variable)
# 숫자와 문자 모두 변수 설정 가능
x = 1
y = 2
z = "hello world"
# 왼쪽에 있는 값이 변수 (x, y, z)
print(x)
print(y)
print(z)



# 타입 (Type)
# 숫자열, 정수와 소수 모두 가능
x = 1
y = 2
z = 1.2
# 기본적인 사칙연산 가능
print(x + y)
print(x - y)
print(x * y)
print(x % y) # x를 y로 나눈 다음에 남는 값 == 나머지
print(x** y)

# 문자열, 큰따옴표와 작은따옴표 가능, 큰따옴표 세개로 줄 바꿈 가능
x = "hello"
y = 'bye'
z = """
안녕하세요 
워니입니다
"""
print(x)
print(y)
print(z)  # <--- 유형은 여러 줄 주석 처리이지만, print 했을 때 값이 나온다 

# 다른 타입을 사칙연산할 때에는 캐스팅해야한다
print("안녕" + " 잘지내니")
print("너 몇살이니? " + str(4) + "살")

x = 4 # 숫자 타입
y = "4" # 문자 타입
print(str(x) + y) # str() 문자 타입으로 캐스팅
print(x + int(y)) # int() 숫자 타입으로 캐스팅



# 불리안 (Boolen)
# 어떤 조건이 참이면 ~~을 해라, 어떤 조건이 거짓이면 ~~을 해라
x = True
y = False

print(x)
print(y)