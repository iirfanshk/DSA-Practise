def replace_elements(nums):
    max_right = nums[-1]

    nums[-1] = -1

    for i in range(len(nums) - 2, -1, -1):
        current = nums[i]
        nums[i] = max_right

        if current > max_right:
            max_right = current

    return nums

nums = list(map(int, input().split()))
print(replace_elements(nums))