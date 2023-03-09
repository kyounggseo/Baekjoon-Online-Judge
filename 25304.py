total = int(input())
type= int(input())
sum=0
 
for _ in range(type):
    while type:
        try:
            a, b= map(int, input().split())
            type -= 1
            sum += a*b
        except:
            break
        
if total == sum: 
    print("Yes")
else: 
    print("No")

