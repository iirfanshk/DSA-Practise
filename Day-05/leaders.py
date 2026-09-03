def find_leaders(arr):
    leaders = []
    n = len(arr)
    max = float('-inf')
    for i in range(n-1,-1,-1):
        if arr[i] > max:
            max = arr[i]
            leaders.append(max)
    return leaders[::-1]
arr = list(map(int, input().split()))
print(find_leaders(arr))
            