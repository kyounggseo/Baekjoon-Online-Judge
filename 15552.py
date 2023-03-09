import sys 

timer = int(sys.stdin.readline())

for _ in range(timer):
    a,b = map(int, sys.stdin.readline().split())
    print(a+b)