# 121
# user = input("입력: ")
# if user.islower() == True:
#   print(user.upper())
# else:
#   print(user.lower())

# 122
# user = int(input("score: "))
# if 100 >= user >= 81:
#   print("grade is A")
# elif 80 >= user >= 61:
#   print("grade is B")
# elif 60 >= user >= 41:
#   print("grade is C423")
# elif 40 >= user >= 21:
#   print("grade is D")
# else:
#   print("grade is E")


"""오답"""
# 123
# user = input("입력: ") # 100 달러 -> 문자열 분리 필요 split() -> 결과값 list()
# money = user.split() # ["100", "달러"]
# num, currency = money # --> num = money[0];num = money[1]
# 외화 = {"달러" : 1167,
# "엔" : 1.096,
# "유로" : 1268,
# "위안" : 171,
# }
# print(float(num) * 외화[currency], "원") # float() 실수로 만들어 줌 0.0


# 124
# user1 = int(input("number1: "))
# user2 = int(input("number2: "))
# user3 = int(input("number3: "))
# if user1 >= user2 and user1 >= user3:
#   print(user1)
# elif user2 >= user1 and user2 >= user3:
#   print(user3)
# else:
#   print(user3)

# print(max(user1, user2, user3))

# 125
# 번호 = {
#   "011" : "SKT",
#   "016" : "KT",
#   "019" : "LGU",
#   "010" : "알 수 없음",
# }
# phone_number = input("휴대전화 번호 입력: ")
# a = phone_number.split("-")
# b = a[0]
# print("당신은 " + 번호[b] + " 사용자입니다.")

# 다른 풀이
# phone_number = input("휴대전화 번호 입력: ")
# a = phone_number.split("-")
# num = a[0]
# if num == "011":
#   com = "SKT"
# elif num == "016":
#   com = "KT"
# elif num == "019":
#   com = "LGU"
# else:
#   com = "알수없음"
# print(f"당신은 {com} 사용자 입니다.") # f-string 사용

# 126
# post_num = input("우편번호: ")
# a = list(post_num)
# b = int(a[2])
# num = {
#   0 : "강북구",
#   1 : "강북구",
#   2 : "강북구",
#   3 : "도봉구",
#   4 : "도봉구",
#   5 : "도봉구",
#   6 : "노원구",
#   7 : "노원구",
#   8 : "노원구",
#   9 : "노원구",
# }
# print(num[b])

# 다른 풀이
# 우편번호 = input("우편번호: ")
# 우편번호 = 우편번호[:3]
# if 우편번호 in ["010", "011", "012"]:
#   print("강북구")
# elif 우편번호 in ["014", "015", "016"]:
#   print("도봉구")
# else:
#   print("노원구")

# 127
# 주민등록번호 = input("주민등록번호: ")
# 성별 = 주민등록번호.split("-")
# a = 성별[1]
# if a[0] == "1" or a[0] == "3":
#   print("남자")
# else:
#   print("여자")

# 128
# 주민등록번호 = input("주민등록번호: ")
# 지역 = 주민등록번호.split("-")
# a = 지역[1]
# b = int(a[1:3])
# if 8 >= b >= 0:
#  print("서울입니다.")
# elif 12 >= b >= 9:
#   print("부산입니다.")
# else:
#   print("타지역입니다.")

# 129
# 주민등록번호 = input("주민등록번호: ")
# split = 주민등록번호.split("-")
# first_num = list(split[0])
# second_num = list(split[1])
# a = (int(first_num[0]) * 2) + (int(first_num[1]) * 3) + \
#     (int(first_num[2]) * 4) + (int(first_num[3]) * 5) + \
#     (int(first_num[4]) * 6) + (int(first_num[5]) * 7)
# b = (int(second_num[0]) * 8) + (int(second_num[1]) * 9) + \
#     (int(second_num[2]) * 2) + (int(second_num[3]) * 3) + \
#     (int(second_num[4]) * 4) + (int(second_num[5]) * 5)
# c = 11 - ((a + b) % 11)
# if int(주민등록번호[13]) != c:
#   print("유효하지 않은 주민등록번호입니다.")
# else:
#   print("유효한 주민등록번호입니다.")

# 다른 풀이
# num = input("주민등록번호: ")
# 계산1 = int(num[0]) * 2 + int(num[1]) * 3 + int(num[2]) * 4 + int(num[3]) * 5 + int(num[4]) * 6 + \
#         int(num[5]) * 7 + int(num[7]) * 8 + int(num[8]) * 9 + int(num[9]) * 2 + int(num[10])* 3 + \
#         int(num[11])* 4 + int(num[12]) * 5
# 계산2 = 11 - (계산1 % 11)
# 계산3 = str(계산2)

# if num[-1] == 계산3[-1]:
#   print("유효한 주민등록번호입니다.")
# else:
#   print("유효하지 않은 주민등록번호입니다.")


"""오답"""
# 130
# import requests
# btc = requests.get("https://api.bithumb.com/public/ticker/").json()['data']
# 변동폭 = float(btc["max_price"]) - float(btc["min_price"])
# 시가 = float(btc["opening_price"])
# 종가 = float(btc["closing_price"])
# 최고가 = float(btc["max_price"])
# 최저가 = float(btc["min_price"])

# if (시가 + 변동폭) >= 최고가:
#   print("상승장")
# else:
#   print("하락장")