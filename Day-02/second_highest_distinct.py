def find_second_highest(numbers):
    highest = second = float('-inf')
    for num in numbers:
        if num > highest:
            second = highest
            highest = num
        elif num > second and num != highest:
            second = num
    return second


n = int(input())
numbers = list(map(int, input().split()))

print(find_second_highest(numbers))