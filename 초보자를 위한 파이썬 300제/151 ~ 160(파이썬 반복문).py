# 151
리스트 = [3, -20, -3, 44]

for 변수 in 리스트:
  if 변수 < 0:
    print(변수)

# 152
리스트 = [3, 100, 23, 44]
for 변수 in 리스트:
  if 변수 % 3 == 0:
    print(변수)

# 153
리스트 = [13, 21, 12, 14, 30, 18]
for 변수 in 리스트:
  if 변수 < 20 and 변수 % 3 == 0:
    print(변수)

# 154
리스트 = ["I", "study", "python", "language", "!"]
for 변수 in 리스트:
  if len(변수) >= 3:
    print(변수)

# 155
리스트 = ["A", "b", "c", "D"]
for 변수 in 리스트:
  if 변수.isupper() == True:
    print(변수)

# 156
리스트 = ["A", "b", "c", "D"]
for 변수 in 리스트:
  if 변수.isupper() == False:
    print(변수)

# 다른 풀이
리스트 = ["A", "b", "c", "D"]
for 변수 in 리스트:
  if not 변수.isupper():
    print(변수)

# 다른 풀이
리스트 = ["A", "b", "c", "D"]
for 변수 in 리스트:
  if 변수.isupper() != True:
    print(변수)

# 157
리스트 = ['dog', 'cat', 'parrot']
for 변수 in 리스트:
  print(변수.upper()[0] + 변수[1:])

# 158
리스트 = ['hello.py', 'ex01.py', 'intro.hwp']
for 변수 in 리스트:
  print(변수.split(".")[0])

# 159
리스트 = ['intra.h', 'intra.c', 'define.h', 'run.py']
for 변수 in 리스트:
  if 변수.split(".")[1] == "h":
    print(변수)

# 160
리스트 = ['intra.h', 'intra.c', 'define.h', 'run.py']
for 변수 in 리스트:
  if 변수.split(".")[1] == "h" or 변수.split(".")[1] == "c":
    print(변수)