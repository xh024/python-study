print("철수: 안녕 영희야")
print("영희: 안녕 뭐해")


# 위 문구를 5번 반복하고 싶다면? 반복문 사용
# for, while
# 예제 1
for i in range(3):
  print(i) # 변수인 i만 실행되기 때문에 0 ~ 9 까지 숫자가 나타난다
  print("철수: 안녕 영희야")
  print("영희: 안녕 뭐해")
# i라는 변수에 해당 문구들을 넣고 10번 반복해라



# 예제 2
# while문은 조건 설정이 가능하다
i = 0
while i < 3: # i가 3보다 작으면 밑에 있는 코드를 실행시켜라
  print(i)
  print("철수: 안녕 영희야")
  print("영희: 안녕 뭐해")
  i = i + 1 # 여기까지 코드가 왔다가 다시 올라간다.



# 예제 3
i = 0
while True: # while 반복문이 계속 실행됨 == 무한루프
  print(i)
  print("철수: 안녕 영희야")
  print("영희: 안녕 뭐해")
  i = i + 1

  if i > 2: # i가 2보다 크면 멈춘다
    break
# break, continue로 멈출 수 있음



# 예제 4 
for i in range(3):
  print(i)
  print("철수: 안녕 영희야")
  print("영희: 안녕 뭐해")
  
  if i == 1: # 특이한 조건에서 밑 코드를 실행시키고 싶지 않을 때 continue 사용
    # 조건(만약 i가 1일 때 밑 코드를 실행시키고 싶지 않다) == i <> 1일 때 밑의 코드가 실행된다
    continue # 반복문이 실행되다가 continue를 만나게되면 코드 끝까지 내려가지 않고 다시 반복되게 됨

  print("정호: 안녕 철수, 영희야") # continue 때문에 실행되지 않음