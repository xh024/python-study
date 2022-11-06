# 041
ticker = "btc_krw"
a = ticker.upper()
print(a)

# 042
ticker = "btc_krw"
a = ticker.lower()
print(a)

# 043
# .capitalize() 첫 문자 대문자로 교체
a = "hello"
b = a.capitalize()
print(b)

# 044
# .endswith() 문자 찾기 True / False
file_name = "보고서.xlsx"
a = file_name.endswith("xlsx")
print(a)

# 045
file_name = "보고서.xlsx"
a = file_name.endswith("xls")
print(a)

# 046
# startswith 메서드를 사용해서 파일 이름 시작 확인
file_name = "2020_보고서.xlsx"
a = file_name.startswith("2020")
print(a)

# 047
# split() 메서드를 사용하면 문자열에서 공백을 기준으로 분리
a = "hello world"
b = a.split(" ")
print(b)

# 048
ticker = "btc_krw"
a = ticker.split("_")
print(a)

# 049
date = "2020-05-01"
a = date.split("-")
print(a)

# 050
data = "039490     "
a = data.rstrip(" ")
print(a)