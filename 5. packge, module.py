# 라이브러리 == 패키지
# 모듈 == 기능이 들어있는 전체 코드 집합

# 7강 예제
# animal packge
# dog, cat modules
# dog, cat modules can say "hi"

# 예제 1
from animal import dog # animal 패키지에서 dog라는 모듈을 가지고 와줘
from animal import cat # animal  패키지에서 cat이라는 모듈을 가지고 와줘

d = dog.Dog() # instance(사례, 경우)
d.hi()

c = cat.Cat()
c.hi()



# 예제 2
from animal import * # animal 패키지에 있는 모든 모듈을 가지고 와줘

d = Dog()
d.hi()

c = Cat()
c.hi()



# 예제 3 (geopy 패키지, pip install geopy)
from geopy.geocoders import Nominatim # geopy 패키지에서 geocoders 모듈로 들어가서 Nominatim 이라는 클래스를 가지고 와줘
# from animal.dog import Dog과 같음 <- animal 패키지에서 dog모듈로 들어가 Dog 클래스를 가지고 와줘
geolocator = Nominatim(user_agent="jeongho")
location = geolocator.geocode("seoul, south korea")
print(location.address) #location.address, location.latitude, location.longitude, location.raw