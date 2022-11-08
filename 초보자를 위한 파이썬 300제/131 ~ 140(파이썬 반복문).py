# 131
과일 = ["사과", "귤", "수박"]
for 변수 in 과일:
    print(변수)
# 사과, 귤, 수박이 하나씩 출력된다.

# 132
과일 = ["사과", "귤", "수박"]
for 변수 in 과일:
  print("#####")
# for문은 과일 list안에 있는 데이터 만큼 코드가 실행된다, ### 세 번 실행

# 133
for 변수 in ["A", "B", "C"]:
  print(변수)

변수 = "A"
print(변수)
변수 = "B"
print(변수)
변수 = "C"
print(변수)

# 134
for 변수 in ["A", "B", "C"]:
  print("출력:", 변수)

변수 = "A"
print("출력: " + 변수)
변수 = "B"
print("출력: " + 변수)
변수 = "C"
print("출력: " + 변수)

# 135
for 변수 in ["A", "B", "C"]:
  b = 변수.lower()
  print("변환:", b)

변수 = "A"
print("변환: " + 변수.lower())
변수 = "B"
print("변환: " + 변수.lower())
변수 = "C"
print("변환: " + 변수.lower())

# 136
변수 = 10
print(변수)
변수 = 20
print(변수)
변수 = 30
print(변수)

리스트 = [10, 20, 30]
for 변수 in 리스트:
  print(변수)

# 137
print(10)
print(20)
print(30)

for 변수 in [10, 20, 30]:
  print(변수)


"""오답"""
# 138
print(10)
print("-------")
print(20)
print("-------")
print(30)
print("-------")

리스트 = [10, 20, 30]
for 변수 in 리스트:
  print(변수)
  print("-------") # for문은 리스트안 요소의 개수에 따라 반복되기 때문에 "------"도 가능하다


# 139
print("++++")
print(10)
print(20)
print(30)

print("++++") # 파이썬 for문은 반복되는 함수에만 사용된다
list = [10, 20, 30]
for 변수 in list:
  print(변수)

# 140
print("-------")
print("-------")
print("-------")
print("-------")

list = [1, 2, 3, 4]
for 변수 in list:
  print("-------")