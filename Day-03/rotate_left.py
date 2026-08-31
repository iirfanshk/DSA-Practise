def rotate_left(numbers):
    first = numbers[0]
    for i in range(len(numbers) - 1):
        numbers[i] = numbers[i + 1]
    numbers[len(numbers) - 1] = first


n = int(input())
numbers = list(map(int, input().split()))

rotate_left(numbers)

print(numbers)