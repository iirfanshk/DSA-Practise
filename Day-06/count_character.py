def count_characters(text):
    vowels_count = 0
    consonants_count = 0
    space_count = 0
    digit_count = 0
    
    for ch in text:
        if ch.lower() in "aeiou":
            vowels_count+=1
        elif ch.isdigit():
            digit_count+=1
        elif ch == " ":
            space_count+=1
        else:
            consonants_count+=1
    return vowels_count,consonants_count,space_count,digit_count
vowels, consonants, space, digits = count_characters("KodNest 2026")

print(f"Vowels: {vowels}")
print(f"Consonants: {consonants}")
print(f"Digits: {digits}")
print(f"Spaces: {space}")
        