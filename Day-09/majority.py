def majority(nums):
    freq = {}
    threshold = len(nums) // 2
    
    # Build a frequency map
    for n in nums:
        freq[n] = freq.get(n,0) + 1
    for n in nums:
        if freq[n] > threshold:
            return n
    return -1

nums = list(map(int, input().split()))
print(majority(nums))