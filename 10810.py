N, M = map(int, input().split())
arr = [0]* (N + 1)
for _ in range(M) :
    i,j,k = map(int, input().split())
    for y in range (i, j+1) :
        arr[y] = k
arr.remove(arr[0])
print(*arr) # print(*list) 배열 띄어쓰기로 구분해서 print하기
