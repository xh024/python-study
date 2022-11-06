# 031
a = "3"
b = "4"
print(a + b)
# a, b는 string이기 때문에 문자가 이어진 34가 나올 것이다.

# 032
print("hi" * 3)
# hihihi

# 033
print("-" * 80)

# 034
t1 = 'python'
t2 = 'java'
print((t1 + " " + t2 + " ") * 4)

t3 = t1 + " " + t2 + " "
print(t3 * 4)

# 035
name1 = "김민수" 
age1 = 10
name2 = "이철희"
age2 = 13
print("이름: %s 나이: %d" %(name1, age1));print("이름: %s 나이: %d" %(name2, age2))
# %s 문자
# %d 숫자
# %f 소수

# 036
# {} .format
name1 = "김민수" 
age1 = 10
name2 = "이철희"
age2 = 13
print("이름: {} 나이: {}"  .format(name1, age1))
print("이름: {} 나이: {}"  .format(name2, age2))

# 037
# f {string}
name1 = "김민수" 
age1 = 10
name2 = "이철희"
age2 = 13
print(f"이름: {name1} 나이: {age1}")
print(f"이름: {name2} 나이: {age2}")

# 038
상장주식수 = "5,969,782,550"
a = 상장주식수.replace(",", "")
b = int(a)
print(b)
print(b, type(b))

# 039
분기 = "2020/03(E) (IFRS연결)"
print(분기[:7])


"""오답"""
# 040
# strip 메소드 사용으로 좌우 공백 제거
# 메소드는 객체와 연관되어 사용된다. ex) object.method_name()
data = "   삼성전자    "
a = data.strip(" ")
print(a)