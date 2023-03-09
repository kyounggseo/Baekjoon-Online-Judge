#H, M = map(int, input().split())
H = int(input())
M = int(input())

timer = int(input()) 

H += timer // 60 #몫
M += timer % 60 #나머지

if M >= 60:
    H += 1
    M -= 60
if H >= 24:
    H -= 24

print(H,M)