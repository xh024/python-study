# class는 함수와 변수들의 합 (==빵틀)
# object는 class를 이용해 만들어낸 물체 (==빵)


#인터넷 예제
# class를 사용하지 않았을 때
def some_function(something):
  print(something)

# 위 코드를 class를 사용할 때
class Someclass:
  def __init__(self, something): # __init__의 첫번째 인수는 무조건 self
    self.something = something

  def some_function1(self): # 메소드 (class내 여러 개의 메소드 정의 가능)
    print(self.something)

  def some_function2(self): # 메소드
    return self.something

a = Someclass("some_value") # 클래스의 인스턴스가 a에 할당
a.some_function1()




# 6강 예제
# 예제 1
class Person:
  name = "정호" # 변수를 넣어도 된다

  def say_hello(self): # 함수
    print("안녕 나는 " + self.name) # 안녕 나는 정호

p = Person()
p.say_hello()



# 예제 2
class Person:
  def __init__(self, name): # 함수, __init__ Person이라는 오브젝트를 만들 때 name이라는 인자를 받아서 name이라는 변수 안에 그 값을 넣어라
    self.name = name

  def say_hello(self, to_name): # 함수, to_name은 인자
    print("안녕 " + to_name + ", 난 " + self.name)

jeongho = Person("정호") # class 이름
leo = Person("레오")
happy = Person("행복")

jeongho.say_hello("레오") # 함수(def) 이름
leo.say_hello("행복")
happy.say_hello("정호")



# 예제 3
class Person:
  def __init__(self, name, age): #함수 안에 인자 추가 가능 (name, age)
    self.name = name
    self.age = age

  def say_hello(self, to_name): # 함수
    print("안녕 " + to_name + ", 난 " + self.name + " " + str(self.age) + "살이야!") #나이는 숫자이므로 str로 캐스팅하기

  def introduce(self):
    print("내 이름은 " + self.name + " 그리고 나는" + str(self.age) + "살이야!")

jeongho = Person("정호", 24)
leo = Person("레오", 5)
happy = Person("행복", 5)

jeongho.say_hello("레오")
leo.say_hello("행복")
happy.say_hello("정호")

jeongho.introduce()
leo.introduce()
happy.introduce()



# 예제 4
class Police(Person): # Police class가 Person class를 상속한다 == 종속
  def arrest(self, to_arrest):
    print("넌 체포됐다! " + to_arrest)

# Police class 안에
"""
  def __init__(self, name, age):
   self.name = name
   self.age = age

  def say_hello(self, to_name):
   print("안녕 " + to_name + ", 난 " + self.name + " " + str(self.age) + "살이야!")

  def introduce(self):
   print("내 이름은 " + self.name + " 그리고 나는" + str(self.age) + "살이야!")
"""
# Person 코드가 있는 것과 같다.

class Progrmer(Person): # Programer class가 Person class를 상속한다
  def program(self, to_program):
    print("다음엔 뭘 만들지? " + to_program + "! 이걸 만들어야겠다!")

jeongho = Person("정호", 24) # class
leo = Police("레오", 5)
happy = Progrmer("행복", 5)

jeongho.introduce() # 함수
leo.arrest("정호")
happy.program("일기예보")
