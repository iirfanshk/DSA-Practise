def remove_duplicates(numbers):
    left = 1
    for right in range(1, len(numbers)):

        if numbers[right] != numbers[right - 1]:
            numbers[left] = numbers[right]
            left+=1
    return left


n = int(input())
numbers = list(map(int, input().split()))

unique_count = remove_duplicates(numbers)

print(unique_count)
print(*numbers[:unique_count])