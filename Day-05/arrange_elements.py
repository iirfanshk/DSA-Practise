def arrange_elements(nums):
    n = len(nums)
    left = 0
    right = n - 1
    
    while left < right:
        if nums[left] %2 == 0:
            left+=1
        elif nums[right] %2 != 0:
            right-=1
        else:
            nums[left],nums[right] = nums[right] , nums[left]
            left+=1
            right-=1
    return nums
nums = list(map(int,input().split()))
print(arrange_elements(nums))
        