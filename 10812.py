n, m = map(int, input().split())
box = [i for i in range(1, n+1)] # box[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for i in range(m):
    i, j, k = map(int, input().split()) 
    # 1 6 4 -> 3 9 8 -> 2 10 5 -> 1 3 3 -> 2 6 2
    box = box[:i-1]+box[k-1:j]+box[i-1:k-1]+box[j:]
print(*box)