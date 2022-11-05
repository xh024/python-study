# 함수 만들기
print("철수: 안녕 넌 몇 살이니?")
print("영희: 나? 나는 12살")


# 위 식을 4번 반복하고 싶다면? 함수 def를 만든다
def chat(): # def + function_name(인자추가 가능):
  print("철수: 안녕 넌 몇 살이니?")
  print("영희: 나? 나는 12살")
# chat() 함수 완성



# print 내용의 이름을 바꾸고 싶다면?
def chat(name1, name2): # def + function_name(인자추가 가능):
  print("%s: 안녕 넌 몇 살이니?" % name1)
  print("%s: 나? 나는 24살" % name2)

chat("정호", "현서")
chat("철수", "영희")
# %s(문자열), %d(정수), %f(실수)



# print 내용에 나이도 추가하려면?
def chat(name1, name2, age): # def + function_name(인자추가 가능):
  print("%s: 안녕 넌 몇 살이니?" % name1)
  print("%s: 나? 나는 %d살" % (name2, age))

chat("정호", "현서", 24)
chat("철수", "영희", 12)
# %s(문자열), %d(정수), %f(실수)



# return 함수
"""
def 함수이름(매개인자):
  수행할 문장
  return 결과값
"""

def dsum(a, b):
  result = a + b #결과값 = a + b
  return result # function을 실행시키면 result라는 변수를 돌려줘라

d = dsum(1, 2) # d == 변수
print(d)



# 예제
# 이름과 나이를 받아라
# 나이가 19살 미만이면 "안녕"
# 나이가 19살에서 20살 사이면 "안녕하세요"
# 그 외에는 "안녕하십니까"라고 하기
def say_hello(name, age):
  if age < 19:
    print("%s야 안녕" % name) # print("안녕, " + name) 가능
  elif age <= 20 and age >= 19:
    print("%s님 안녕하세요" % name) # print("안녕하세요, " + name) 가능
  else:
    print("%s님 안녕하십니까" % name) # print("안녕하십니까, " + name) 가능

say_hello("정호", 24)
say_hello("레오", 5)
say_hello("행복", 5)

# 예제 변형
def say_hello(name, age):
  if age < 19:
    print("안녕, " + name) 
  elif age <= 20 and age >= 19:
    print("안녕하세요, " + name)
  else:
    print("안녕하십니까, " + name)

say_hello("정호", 24)
say_hello("레오", 5)
say_hello("행복", 5)