def find_first_and_last(numbers, target):
    first = -1
    last = -1

    for i in range(len(numbers)):
        if numbers[i]==target:
            if first == -1:
                first = i
            last = i

    return first, last


n = int(input())
numbers = list(map(int, input().split()))
target = int(input())

first, last = find_first_and_last(numbers, target)

print(f"First: {first}")
print(f"Last: {last}")
