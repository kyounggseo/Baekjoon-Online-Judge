s = [i for i in range(1, 31)]

for i in range(28):
    n = int(input())
    s.remove(n)
print(min(s))
print(max(s))