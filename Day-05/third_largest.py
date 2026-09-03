def third_largest(nums):
    first=float('-inf')
    second=float('-inf')
    third=float('-inf')
    
    for i in nums:
        if i > first:
            third = second
            second = first
            first = i
        elif i < first and i > second:
            third = second
            second = i
        elif i < second and i > third:
            third = i
            
            
    return third if third != float('-inf') else -1
nums = list(map(int, input().split()))
print(third_largest(nums))