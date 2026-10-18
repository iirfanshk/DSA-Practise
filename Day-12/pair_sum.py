def find_pair_sum(numbers, target):
    seen = {}

    for i in range(len(numbers)):
        diff = target - numbers[i]

        if diff in seen:
            return seen[diff], i
        seen[numbers[i]] = i

    return -1

n = int(input())
numbers = list(map(int, input().split()))
target = int(input())

result = find_pair_sum(numbers, target)

if result == -1:
    print(-1)
else:
    print(result[0], result[1])