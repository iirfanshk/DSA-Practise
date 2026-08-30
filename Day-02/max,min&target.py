def analyse_array(numbers, target):
    maximum = numbers[0]
    minimum = numbers[0]
    found = False

    for i in numbers:
        if i > maximum:
            maximum=i
        if i < minimum:
            minimum=i
        if i==target:
            found = True

    return maximum, minimum, found


n = int(input())
numbers = list(map(int, input().split()))
target = int(input())

maximum, minimum, found = analyse_array(numbers, target)

print(f"Maximum: {maximum}")
print(f"Minimum: {minimum}")
print(f"Target Found: {'Yes' if found else 'No'}")