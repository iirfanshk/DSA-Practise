def target_sum_subarray(numbers, target):
    seen ={0: -1}
    running = 0
    for i in range(len(numbers)):
        running += numbers[i]

        if running - target in seen:
            return seen[running - target] +1 , i

        if running not in seen:
            seen[running] = i

    return -1


n = int(input())
numbers = list(map(int, input().split()))
target = int(input())

result = target_sum_subarray(numbers, target)

if result == -1:
    print(-1)
else:
    print(result[0], result[1])