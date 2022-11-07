"""오답"""
# 081
# 데이터 언패킹
a, b = (1, 2) # 튜플에 두개의 요소가 있을 때, a = 1, b = 2
a, b, *c = (1, 2, 3, 4, 5) # 튜플의 개수가 맞지 않을 때, *c가 나머지 값 바인딩
print(a) # 1
print(b) # 2
print(c) # 3, 4, 5

scores = [8.8, 8.9, 8.7, 9.2, 9.3, 9.7, 9.9, 9.5, 7.8, 9.4]
*valid_score, a, b = scores # 나머지 값 두개를 a = 7.8, b = 9.4
print(valid_score)

scores = [8.8, 8.9, 8.7, 9.2, 9.3, 9.7, 9.9, 9.5, 7.8, 9.4]
scores.sort()
print(scores)
a, *b, c = scores
print(a) # 최저점
print(b) # 중간값
print(c) # 최고점


# 082
scores = [8.8, 8.9, 8.7, 9.2, 9.3, 9.7, 9.9, 9.5, 7.8, 9.4]
a, b, *valid_score = scores
print(a)
print(b)
print(valid_score)

# 083
scores = [8.8, 8.9, 8.7, 9.2, 9.3, 9.7, 9.9, 9.5, 7.8, 9.4]
a, *valid_score, b = scores
print(a)
print(valid_score)
print(b)

# 084
temp = {}

# 085
ice_creams = {
  "메로나" : 1000,
  "폴라포" : 1200,
  "빵빠레" : 1800,
}
print(ice_creams)

# 086
ice_creams = {
  "메로나" : 1000,
  "폴라포" : 1200,
  "빵빠레" : 1800,
}
ice_creams["죠스바"] = 1200
ice_creams["월드콘"] = 1500
print(ice_creams)

# 087
ice = {'메로나': 1000,
       '폴로포': 1200,
       '빵빠레': 1800,
       '죠스바': 1200,
       '월드콘': 1500}
print("메로나 가격:", ice["메로나"])

# 088
ice = {'메로나': 1000,
       '폴로포': 1200,
       '빵빠레': 1800,
       '죠스바': 1200,
       '월드콘': 1500}
ice["메로나"] = 1300
print(ice)

# 089
ice = {'메로나': 1000,
       '폴로포': 1200,
       '빵빠레': 1800,
       '죠스바': 1200,
       '월드콘': 1500}
del ice["메로나"]
print(ice)

# 090
# icecream = {'폴라포': 1200, '빵빠레': 1800, '월드콘': 1500, '메로나': 1000}
# icecream['누가바']
# 딕셔너리에 존재하지 않는 key를 사용해 오류가 발생했다