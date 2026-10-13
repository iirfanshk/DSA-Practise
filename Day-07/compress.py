def compress_chars(text):
    result = []
    n = len(text)
    consecutive_count = 1
    
    for i in range(1,n):
        if text[i] == text[i-1]:
            consecutive_count+=1
        else:
            result.append(text[i-1] + str(consecutive_count))
            consecutive_count = 1
    result.append(text[-1] + str(consecutive_count))
    
    return "".join(result)
text = input()
print(compress_chars(text))