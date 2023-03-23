n = int(input())
nums = list(map(int, input()))
sum = 0
for i in range(n):
    sum += int(nums[i])
print(sum)