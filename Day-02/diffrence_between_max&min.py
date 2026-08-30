def max_min_difference(numbers):
    maximum = numbers[0]
    minimum = numbers[0]

    # Write your traversal logic here
    for i in numbers:
        if i > maximum:
            maximum = i
        if i < minimum:
            minimum = i

    return maximum - minimum


n = int(input())
numbers = list(map(int, input().split()))

print(max_min_difference(numbers))