# list 
# 유형 [], element 여러개를 grouping 할 때 쓰임
x1 = list()
y1 = []

print(x1)
print(y1)


# 예시
a1 = [1, 2, 3, 4] # 숫자
b1 = ["hello", "jeongho", "leo"] # 문자
c1 = ["hello", 2, 3, 4] # 숫자 + 문자

print(a1)
print(b1)
print(c1)
print(a1 + b1) # 각 list 병합 가능


# a1 요소의 0번 째 자리를 보여줘 (list의 size보다 크게 되면 error 발생)
print(a1[0])


# a1 요소의 0번 째 자리를 10으로 바꿔주고, 보여줘
a1[0] = 10
print(a1)


# list elements 개수 function
num_elements1 = len(a1)
print(num_elements1)


# list elements 정렬 function
num_elements2 = sorted(a1)
print(num_elements2)


# list elements 합 function
num_elements3 = sum(a1)
print(num_elements3)


# 반복문 +  list
for num_elements4 in a1: # list elements를 하나씩 돌아가면서 나한테 보여줘
  print(num_elements4) # 10, 2, 3, 4 차례대로 보여줌


# index로 list elements 자리 찾기
print(a1.index(10)) # a1 list의 elements 중 10은 어느자리에 있어?
# list에 값이 없는 경우 error


# in으로 자리가 아닌 list에 요소가 존재하는지 확인
print("hello" in b1) # hello가 b1 list안에 있어? true / false
# in과 list를 사용한 if문
if "hello" in b1:
  print("hello가 있어요!")
else:
  print("hello가 없어요!")