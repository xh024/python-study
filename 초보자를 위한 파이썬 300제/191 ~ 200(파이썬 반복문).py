# 191
data = [
    [ 2000,  3050,  2050,  1980],
    [ 7500,  2050,  2050,  1980],
    [15450, 15050, 15550, 14900]
]
for line in data:
  for column in line:
    print(column * 1.00014)

# 192
data = [
    [ 2000,  3050,  2050,  1980],
    [ 7500,  2050,  2050,  1980],
    [15450, 15050, 15550, 14900]
]
for line in data:
  for column in line:
    print(column * 1.00014)
  print("-" * 4)


"""오답"""
# 193
data = [
    [ 2000,  3050,  2050,  1980],
    [ 7500,  2050,  2050,  1980],
    [15450, 15050, 15550, 14900]
]
result = [ ]
for line in data:
  for column in line:
    result.append(column * 1.00014)
  print(result)


"""오답"""
# 194
data = [
    [ 2000,  3050,  2050,  1980],
    [ 7500,  2050,  2050,  1980],
    [15450, 15050, 15550, 14900]
]
result = [ ]
for 층 in data:
  sub = [ ]
  for 요소 in 층:
    sub.append(요소 * 1.00014)
    result.append(sub)
print(result)


"""오답"""
# 195
ohlc = [["open", "high", "low", "close"],
        [100, 110, 70, 100],
        [200, 210, 180, 190],
        [300, 310, 300, 310]]
for i in ohlc[1 : ]: # ohlc의 o 제외
  print(i[3])


# 196
ohlc = [["open", "high", "low", "close"],
        [100, 110, 70, 100],
        [200, 210, 180, 190],
        [300, 310, 300, 310]]
for i in ohlc[1 : ]:
  if i[3] >= 150:
    print(i[3])

# 197
ohlc = [["open", "high", "low", "close"],
        [100, 110, 70, 100],
        [200, 210, 180, 190],
        [300, 310, 300, 310]]
for i in ohlc[1 : ]:
  if i[3] >= i[0]:
    print(i[3])


# 198
ohlc = [["open", "high", "low", "close"],
        [100, 110, 70, 100],
        [200, 210, 180, 190],
        [300, 310, 300, 310]]
volatility = [ ]
for i in ohlc[1 : ]:
  변동폭 = i[1] - i[2]
  volatility.append(변동폭)
print(volatility)

# 다른 풀이
ohlc = [["open", "high", "low", "close"],
        [100, 110, 70, 100],
        [200, 210, 180, 190],
        [300, 310, 300, 310]]
volatility = [ ]
for i in range(1, len(ohlc)):
  volatility.append(ohlc[i][1]-ohlc[i][2])
print(volatility)

# 199
ohlc = [["open", "high", "low", "close"],
        [100, 110, 70, 100],
        [200, 210, 180, 190],
        [300, 310, 300, 310]]
for i in ohlc[1 : ]:
  if i[3] > i[0]:
    print(i[1] - i[2])


"""오답"""
# 200
# 총 수익금 구하는 방식
ohlc = [["open", "high", "low", "close"],
        [100, 110, 70, 100],
        [200, 210, 180, 190],
        [300, 310, 300, 310]]
total = 0 # 처음 값 0임
for i in ohlc[1 : ]:
  수익금 = i[0] - i[3] # 각 거래일 수익금
  total = total + 수익금 # total에 수익금이 점차 누적된다
print(total)