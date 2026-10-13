def build_frequency_map(text):
    frequency = {}

    # Build and return the character-frequency map
    for ch in text:
        if ch in frequency:
            frequency[ch] = frequency[ch] + 1
        else:
            frequency[ch] = 1

    return frequency


def are_anagrams(first, second):
    if len(first)!=len(second):
        return False

    return build_frequency_map(first) == build_frequency_map(second) 

first = input()
second = input()

if are_anagrams(first, second):
    print("Anagrams")
else:
    print("Not Anagrams")