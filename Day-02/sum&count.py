def calculate_sum_and_count(numbers):
    total = 0
    count = 0
    for i in numbers:
        total = total + i
        count = count + 1

    return total, count


n = int(input())
numbers = list(map(int, input().split()))

total, count = calculate_sum_and_count(numbers)

print(f"Sum: {total}")
print(f"Count: {count}")