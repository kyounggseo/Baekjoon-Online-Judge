n, m = map(int, input().split())

arr = [i for i in range(1, n+1)]

for _ in range(m): # 0,1,2,3
    i, j = map(int, input().split())
    arr[i-1:j] = arr[i-1:j][::-1]
print(*arr) #리스트 요소의 값 한줄로 출력