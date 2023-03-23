n = int(input())
new = []
jumsu = list(map(int, input().split()))
max = max(jumsu)

for i in jumsu:
    new.append(i/max*100)
print(sum(new)/n)
