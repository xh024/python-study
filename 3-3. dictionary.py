# dictionary
# 유형 {}, key와 value로 이루어짐, key 값은 불변하는 값만 가능하므로 가변하는 list는 불가능
x3 = dict()
y3 = {}

print(x3)
print(y3)

# 예제 1
a3 = {
  "name" : "정호",
  "age" : 24,
  "adrress" : "서울 강동구 아리수로93가길 110",
}

# 전체 dict 값 표현
print(a3)

# a3 dict key의 value가 무엇인가?
print(a3["name"])
print(a3["age"])



# 예제 2
b3 = {
  0 : "jeongho",
  1 : "hello",
  "age" : 24,
}

print(b3[0])
print(b3[1])
print(b3["age"])

# age라는 키가 b3 dict에 들어있나요?
print("age" in b3) # true / false

# b3 dict의 모든 key를 보여주세요
print(b3.keys())
#b3 dict의 모든 value를 보여주세요
print(b3.values())


# 하나씩 보여주세요
for key in b3:
  print("key: " + str(key))
  print("value: " + str(b3[key]))


# b3 dict 내 0 key의 value를 현서로 바꾸기
b3[0] = "현서"
print(b3)


# key와 value를 새로 추가하기
b3["school"] = "한빛"
print(b3)



# 프로그램 짜기
fruit = ["사과", "사과", "사과", "바나나", "바나나", "키위", "딸기", "복숭아", "복숭아"]
# fruit이라는 list안에 과일이 몇개 씩 있는지 확인해보기

a = {}
# 처음엔 dict가 비어있음
for f in fruit: # for 변수 in 객체(list, tuble, dict), 하나씩 반복되기 시작한다
  if f in a: # a라는 dict에 "사과" 라는 key가 들어있어?
    a[f] = a[f] + 1 # 그럼 갯수를 하나 올려줘
  else:
    a[f] = 1 # 근데 "사과" 라는 key가 없으면, 그걸 dixt에 넣고 1로 만들어줘

print(a)