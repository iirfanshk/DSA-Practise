def remove_duplicate_char(text):
    result = " "
    for i in text:
        if len(result) == 0 or result[-1] != i:
            result = result + i
    return result
text = "aaabbcdd"
print(remove_duplicate_char(text)) 
        