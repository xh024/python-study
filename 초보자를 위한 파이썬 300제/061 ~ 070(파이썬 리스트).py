# 061
price = ['20180728', 100, 130, 140, 150, 160, 170]
print(price[1:])

# 062
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(nums[::2]) # nums[start : end : offset]

# 063
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(nums[1::2])

# 064
nums = [1, 2, 3, 4, 5]
print(nums[::-1])

# 065
interest = ['삼성전자', 'LG전자', 'Naver']
print(interest[0], interest[2])


"""오답"""
# 066
interest = ['삼성전자', 'LG전자', 'Naver', 'SK하이닉스', '미래에셋대우']
a = " ".join(interest)
print(a)


# 067
interest = ['삼성전자', 'LG전자', 'Naver', 'SK하이닉스', '미래에셋대우']
a = "/".join(interest)
print(a)


"""오답"""
# 068
# 이스케이프 시퀀스 \n: 줄바꿈, \t: tap키, \0: null값, \\: \표시, \'\': '표시
interest = ['삼성전자', 'LG전자', 'Naver', 'SK하이닉스', '미래에셋대우']
a = "\n".join(interest)
print(a)


"""오답"""
# 069
# .split('구분자', '분할횟수') 문자열 나누기
string = "삼성전자/LG전자/Naver"
interest = string.split("/")
print(interest)


"""오답"""
# 070
# sorted 오름차순
data = [2, 4, 3, 1, 5, 10, 9]
a = sorted(data)
print(a)

data.sort()
print(data)