def second_largest(arr):
    largest = float('-inf') 
    second = float('-inf')
    
    for i in arr:
        if i > largest:
            second = largest
            largest = i
        elif i < largest and i > second:
            second = i
        
    return second if second != float('-inf') else -1
arr = list(map(int,input().split()))
print(second_largest(arr))