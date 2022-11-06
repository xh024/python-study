# 021
letters = 'python'
print(letters[0], letters[2])

# 022
license_plate = "24가 2210"
print(license_plate[4:])
print(license_plate[-4:])


"""오답"""
# 023 
# # 슬라이싱(원하는 부분 추출) 사용
# [start : end] start 부터 end -1 까지
# [start : end : step] step 만큼 문자를 건너 띔
string = "홀짝홀짝홀짝"
print(string[0: :2]) # <---- 0부터 끝까지, 오프셋 2개씩 이동하기
print(string[0], string[2], string[4], sep = "") # <---- sep으로 띄어쓰기 없애주기 


"""오답"""
# 024
string = "PYTHON"
print(string[::-1]) # <---- 외우기, 뒤집는 표현


"""오답"""
# 025
# 변수.replace("Old text", "New text") 사용
phone_number = "010-1111-2222"
phone_number_replace = phone_number.replace("-"," ")
print(phone_number_replace)


# 026
phone_number = "010-1111-2222"
phone_number_replace = phone_number.replace("-", "")
print(phone_number_replace)


"""오답"""
# 027
url = "http://sharebook.kr"
# 도메인이 kr인 경우, com인 경우 등이 있다
#"."을 기준으로 문자열을 잘라준다 (변수.split()사용)
url_split = url.split(".") # ['http://sharebook', 'kr']
print(url_split[1]) # url_split[0]이면 주소 발현
# list 사용
print(url[-2:])
# 슬라이싱 사용


# 028
# lang = 'python'
# lang[0] = 'P' # 대문자로 변환 불가
# print(lang)
# 문자열은 수정이 불가능하다

# 029
string = 'abcdfe2a354a32a'
string_replace = string.replace("a", "A")
print(string_replace)

# 030
string = 'abcd'
string.replace('b', 'B')
print(string)
# abcd가 그대로 출력된다
print(string.replace('b', 'B')) # 이렇게 해야 print 된다