def sort_by_second_value(pairs):
    return sorted(pairs, key=lambda pairs: pairs[1])


n = int(input())
pairs = []

for _ in range(n):
    first_value, second_value = map(int, input().split())
    pairs.append((first_value, second_value))

answer = sort_by_second_value(pairs)

for first_value, second_value in answer:
    print(first_value, second_value)