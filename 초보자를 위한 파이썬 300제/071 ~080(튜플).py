# 071
my_variable = ()
print(type(my_variable))

# 072
movie_rank = ("닥터스트레인지", "스플릿", "럭키")


"""오답"""
# 073
num_one = (1, ) # 하나의 데이터만 저장하는 경우 "," 콤마를 사용해야한다

# 074
# t = (1, 2, 3)
# t[0] = 'a'
# tuple은 데이터를 바꾸지 못하기 때문에 오류가 생긴다


"""오답"""
# 075
t = 1, 2, 3, 4
# 튜플은 일반적으로 ()가 필요하지만, 사용자 편의를 위해 괄호 없이도 작동된다


# 076
t = ('a', 'b', 'c')
t = ('A', 'b', 'c')
print(t)
# t[0] = "A"는 tuple에서 작동하지 않으므로 새로운 코드를 작성해야한다


"""오답"""
# 077
interest = ('삼성전자', 'LG전자', 'SK Hynix')
data = list(interest)


"""오답"""
# 078
interest = ['삼성전자', 'LG전자', 'SK Hynix']
data = tuple(interest)
# 딕셔너리 전환은 변수 = dict()


# 079
temp = ('apple', 'banana', 'cake')
a, b, c = temp
print(a, b, c)
# apple balanc cake


"""오답"""
# 080
# (2, 4, 6, 8 ... 98)
# 범위 range(2, 100, 2) -> 2부터 100-1(99)까지의 범위를 2 숫자 만큼 반환
a = tuple(range(2, 100, 2))
print(a)