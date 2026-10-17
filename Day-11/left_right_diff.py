def left_right_difference(numbers):
    sum = 0
    for n in numbers:
        sum += n
        
    left_sum = 0
    answers = []
    for i in range(len(numbers)):
        right_sum = sum - left_sum - numbers[i]
        answers.append(abs(left_sum - right_sum))
        left_sum += numbers[i]
    return answers

numbers = list(map(int, input().split()))

print(*left_right_difference(numbers))
        