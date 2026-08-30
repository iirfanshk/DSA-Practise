def count_even_odd(numbers):
    even_count = 0
    odd_count = 0

    for i in numbers:
        if i%2==0:
            even_count+=1
        else:
            odd_count+=1

    return even_count, odd_count


n = int(input())
numbers = list(map(int, input().split()))

even_count, odd_count = count_even_odd(numbers)

print(f"Even: {even_count}")
print(f"Odd: {odd_count}")