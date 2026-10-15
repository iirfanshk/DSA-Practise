def find_common_values(first, second, third):
    second_values = set(second)
    third_values = set(third)
    added = set()
    result = []

    # Traverse the first array
    # Add values present in both lookup sets only once
    for num in first:
        if num in second_values and num in third_values and num not in added:
            result.append(num)
            added.add(num)

    return result


n = int(input())
first = list(map(int, input().split()))

m = int(input())
second = list(map(int, input().split()))

p = int(input())
third = list(map(int, input().split()))

result = find_common_values(first, second, third)

if result:
    print(*result)
else:
    print(-1)