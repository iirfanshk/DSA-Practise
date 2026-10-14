def build_freq_map(nums):
    frequency = {}
    for n in nums:
        frequency[n] = frequency.get(n , 0) + 1
    return frequency

n = int(input())
numbers = list(map(int, input().split()))

frequency = build_freq_map(numbers)
for number, count in frequency.items():
    print(number, count)