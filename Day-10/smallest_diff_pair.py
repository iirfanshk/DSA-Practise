def smallest_difference_pair(nums):
    ordered = sorted(nums)
    
    smallest_difference = float("inf")
    ans_first = 0
    ans_second = 0
    
    for i in range(1, len(ordered)):
        diff = ordered[i] - ordered[i-1]
        if diff < smallest_difference:
            smallest_difference = diff
            ans_first = ordered[i-1]
            ans_second = ordered[i]
    return ans_first, ans_second

nums = list(map(int, input().split()))
first, second = smallest_difference_pair(nums)
print(first, second)