def equilibrium_index(numbers):
    sum = 0 
    for n in numbers:
        sum+=n

    left_sum = 0
    for i in range(len(numbers)):
        right_sum = sum - left_sum -numbers[i]

        if left_sum == right_sum:
            return i
    
        left_sum += numbers[i]

    return -1
n = int(input())
numbers = list(map(int, input().split()))

print(equilibrium_index(numbers))