# find the largest number in the list
def find_largest(numbers):
    largest = numbers[0]
    for i in numbers:
        if i > largest:
            largest = i
    return largest
n = int(input())
numbers = list(map(int, input().split()))

print(find_largest(numbers))