def move_zeroes(numbers):
    pos = 0
    for i in range(len(numbers)):
        if numbers[i] != 0:
            numbers[pos], numbers[i] = numbers[i], numbers[pos]
            pos += 1
    return numbers


n = int(input())
numbers = list(map(int, input().split()))

result = move_zeroes(numbers)
print(*result)