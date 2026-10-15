def first_non_repeat(numbers):
    freq = {}
    
    # build a frequency map
    for n in numbers:
        freq[n] = freq.get(n,0)+1
    for n in numbers:
        if freq[n] == 1:
            return n
    return -1
numbers = list(map(int, input().split()))
print(first_non_repeat(numbers))