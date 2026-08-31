def reverse_array(nums):
    n = len(nums)
    left = 0
    right = n-1
    
    while left < right:
        nums[left], nums[right] = nums[right], nums[left]
        left+=1
        right-=1
    return nums
nums = list(map(int, input().split()))

reverse_array(nums)
print(nums)
