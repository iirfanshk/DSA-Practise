def find_first_unique_character(text):
    freq = {}
    
    for ch in text:
        if ch in freq:
            freq[ch] = freq[ch] + 1
        else:
            freq[ch] = 1
    for ch in text:
        if freq[ch] == 1:
            return ch
    return"-1"
text = input()
print(find_first_unique_character(text))