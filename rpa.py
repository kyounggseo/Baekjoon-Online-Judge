import datetime as dt

a = dt.datetime(2022, 3, 25)
print(f"a : {a}")
print(f"a의 연도 : {a.year}")
print(f"a의 월 : {a.month}")
print(f"a의 요일 : {a.day}")

b = dt.datetime(2022, 10, 14) 
print(f"b : {b}")
print(f"b의 연도 : {b.year}")
print(f"a의 월 : {b.month}")
print(f"a의 요일 : {b.day}")

diff = abs(a-b)
print(f"사이의 날짜와 시간 : {diff}")
print(f"사이의 날짜 : {diff.days}")