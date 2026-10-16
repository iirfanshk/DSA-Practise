def sort_by_frequency(numbers):
    frequency = {}

    for number in numbers:
        frequency[number] = frequency.get(number, 0) + 1

    sorted_list = sorted(numbers , key = lambda number: (-frequency[number], number))

    return sorted_list


n = int(input())
numbers = list(map(int, input().split()))

answer = sort_by_frequency(numbers)
print(*answer)