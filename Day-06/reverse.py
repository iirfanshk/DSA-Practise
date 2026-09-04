# def reverse(original):
    
#     reversed=[]
#     n = len(original)
#     last = n-1
#     while last>=0:
#         reversed.append(original[last])
#         last-=1
#     return reversed

# original = 'hello'
# print(reverse(original))

def reverse(text):
    
    reversed=''
    n = len(text)
    for i in range(n-1,-1,-1):
        reversed = reversed + text[i]
    return reversed
text='hello'
print(reverse(text))