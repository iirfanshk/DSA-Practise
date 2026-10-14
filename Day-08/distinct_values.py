def count_distinct(numbers):
    distinct_values = set()
    for n in numbers:
        if n not in distinct_values:
            distinct_values.add(n)
    return len(distinct_values)
numbers = list(map(int, input().split()))
print(count_distinct(numbers))
    