def two_sum(numbers,target):
    seen = {}
    
    for i in range(len(numbers)):
        diffrence = target - numbers[i]
        if diffrence in seen:
            return seen[diffrence], i
        seen[numbers[i]] = i
    return -1
n = int(input())
numbers = list(map(int, input().split()))
target = int(input())

result = two_sum(numbers, target)

if result == -1:
    print(-1)
else:
    print(*result)