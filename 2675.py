t = int(input())

for i in range(t):
    r, s = input().split()
    text =''
    for j in s:
        text += int(r) * j
    print(text)
