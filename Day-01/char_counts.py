def count(text):
    uppercase = 0
    lowercase = 0
    digits = 0
    
    for ch in text:
        if ch.isupper():
            uppercase+=1
        elif ch.islower():
            lowercase+=1
        elif ch.isdigit():
            digits+=1
    return uppercase, lowercase, digits
text = input()
uppercase, lowercase, digits = count(text)
print(f"Uppercase: {uppercase}")
print(f"Lowercase: {lowercase}")
print(f"Digits: {digits}")