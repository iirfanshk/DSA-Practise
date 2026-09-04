def reverse(text):
    
    reversed=''
    n = len(text)
    for i in range(n-1,-1,-1):
        reversed = reversed + text[i]
    return reversed
text='hello'
print(reverse(text))