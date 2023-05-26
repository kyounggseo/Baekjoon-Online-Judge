a = "hello World"
print(a)
print(a.upper()) # 모두 대문자로
print(a.capitalize()) # 첫글자만 대문자로
print(a.lower())

b = '가나나나나다라마바사'
print(b.count('나')) # 4
print(b.count('아')) # 0

## find() 사용
c = 'abccccdefg'
print(c.find('c')) # 2
print(c.find('h')) # 값이 없을 시 -1 출력
print(c.rfind('c')) # 5

## index() 사용
print(c.index('c')) # 2
# print(c.index('h')) # 값이 없을 시 error 출력

## startswith() 사용
print(c.startswith('a')) # true

## strip() 사용
d = '         abcde     '
print(d.lstrip())
print(d.rstrip())
print(d.strip())

## split() 사용
e = '보통예금_매출채권_매입채무'
print(e.split(sep= '_')) # ['보통예금', '매출채권', '매입채무']

## replace() 사용
f = '보통예금'
print(f.replace('보통','바꿈')) # 바꿈예금

## zfill() 사용
g = '123'
print(g.zfill(5)) # 00123

## max() 사용
h = ['12', '44', '55', '66']
print(max(h)) # 66

# ## def 사용자 지정 함수 사용 - 1
# a = 100
# def func():
#     b = 1
#     return b
# print(func()) # 1

# ## def 사용자 지정 함수 사용 - 2
# a = 100
# def func():
#     b = a + 1
#     return b

# print(func()) # 101

# ## def 사용자 지정 함수 사용 - 3
# # a = 100
# # def func():
# #     a = a + 1
# #     return a

# # print(func()) # 함수 안에 설정한 a = 'a' + 1 부분에서 'a'인 지역변수의 값이 지정되어 있지 않기 때문에 error

# ## def 사용자 지정 함수 사용 - 4
# a = 100
# def func():
#     a = 1
#     a = a + 20
#     return a

# print(func()) # 21 지역변수의 값이 지정되어 있음

## def 사용자 지정 함수 사용 - 5
ints = 100
def func(ints):
    ints = ints + 20
    return ints

print(func(ints)) # 120

## lambda 함수
plus = lambda x, y : x + y
print(plus(3,5)) # 8

gop = map(lambda x : x * 2, [1,2,3,4,5])
print(list(gop))

ch = ['12', '34', '56']
ch = list(map(float, ch))
print(ch)

