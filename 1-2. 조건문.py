# if문

# 예제 1
if 2 > 1:
  print("hello")
# 2가 1보다 크면 print 해라



#예제 2
if not 1 > 2:
  print("hello")
# 1이 2보다 크지 "않다면" print 해라



# 예제 3
# 조건에 and, or 사용 가능
if 2 > 1 and 3 > 1:
  print("hello")
# 2가 1보다 "크고" 2이 1보다 크면 print 해라

if 0 > 0 or 1 > 0:
  print("hello")
# 0이 0보다 "크거나" 1이 0보다 크면 print 해라



# 예제 4
x = 3 # 변수 설정

if x > 2:
  print("hello")
else:
  print("bye")
# 변수가 2보다 크다면 "hello", 그렇지 않다면 "bye"



# 예제 5
x = 3 # 변수 설정

if x > 5:
  print("hello")
elif x == 3:
  print("hi")
else:
  print("bye")
# 변수가 5보다 크면 "hello", 변수가 3이면 "hi", 아무것도 포함되지 않는다면 "bye"
