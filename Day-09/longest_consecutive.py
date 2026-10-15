def longest_consecutive_length(numbers):
    unique_numbers = set(numbers)
    longest_length = 0

    # Find sequence starts
    # Extend each sequence and update the longest length
    for num in unique_numbers:
        if num - 1 not in unique_numbers:
            current = num
            length = 1

            while current + 1 in unique_numbers:
                current += 1
                length += 1

            if length > longest_length:
                longest_length = length

    return longest_length


n = int(input())
numbers = list(map(int, input().split()))

print(longest_consecutive_length(numbers))