"""오답"""
# 171
price_list = [32100, 32150, 32000, 32500]
for i in price_list:
  print(i)

price_list = [32100, 32150, 32000, 32500]
for i in range(0, 4):
  print(price_list[i])


"""오답"""
# 172
price_list = [32100, 32150, 32000, 32500]
for i in range(0, 4):
  print(i, price_list[i])

# 173
price_list = [32100, 32150, 32000, 32500]
for i in range(0, 4):
  print(3-i, price_list[i])

# 174
price_list = [32100, 32150, 32000, 32500]
for i in range(1, 4):
  print(90 + 10 * i, price_list[i])

# 175
my_list = ["가", "나", "다", "라"]
for i in range(0, 3):
  print(my_list[i], my_list[i+1])

# 176
my_list = ["가", "나", "다", "라", "마"]
for i in range(0, 3):
  print(my_list[i], my_list[i+1], my_list[i+2])


"""오답"""
# 177
my_list = ["가", "나", "다", "라"]
for i in range(0, 3):
  print(my_list[3 - i], my_list[2 - i])

# 178
my_list = [100, 200, 400, 800]
for i in range(0, 3):
  print(my_list[i+1] - my_list[i])


"""오답"""
# 179
my_list = [100, 200, 400, 800, 1000, 1300]
for i in range(0, 4): # 0, 1, 2, 3
  hap = my_list[i] + my_list[i+1] + my_list[i+2]
  print(hap / 3)


"""오답"""
# 180
low_prices  = [100, 200, 400, 800, 1000]
high_prices = [150, 300, 430, 880, 1000]
volatility = [ ] # list에 값 추가하기
for i in range(0, 5):
  diff = high_prices[i] - low_prices[i]
  volatility.append(diff) # append 메소드 생성해서 volatility라는 list에 값 추가
  print(volatility)