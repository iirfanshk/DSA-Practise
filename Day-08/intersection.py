def find_intersection(first, second):
    second_values = set(second)
    added = set()
    result =[]
    
    for num in first:
        if num in second_values and num not in added:
            result.append(num)
            added.add(num)
            
    return result
first = list(map(int,input().split()))
second = list(map(int, input().split()))

result = find_intersection(first, second)

if result:
    print(*result)
else:
    print(-1)