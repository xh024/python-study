# 문자열 출력
name = "홍길동"
phone = "010-0000-0000"
print(name)
print(phone)

print(name + "의 전화번호는 " + phone + "입니다.")



# input 입력
# 예제 1
name = input("이름을 입력하세요")
phone = input("전화번호를 입력하세요")

print(name + "의 전화번호는 " + phone + "입니다.")
print("저장이 완료되었습니다.")



# 예제 2
a = int(input("국어 점수를 입력하세요")) #기본적으로 input은 str이므로 int()로 캐스팅해야함
b = int(input("수학 점수를 입력하세요"))
score = a + b
print("시험 성적의 총 합은", score, "점 입니다.")
print("시험 성적의 평균은", score/2, "점 입니다.")
# 숫자열을 print할 때에는 +가 아닌 , 사용

"""
콤마(,)는 모든 자료형을 연결시킬 수 있지만,
덧셈(+)은 문자열들만 연결할 수 있다
"""