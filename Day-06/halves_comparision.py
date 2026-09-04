def halves_match(text):
    length = len(text)
    if length % 2 != 0:
        return False

    half = length // 2

    for i in range(half):
        if text[i] != text[half + i]:
            return False

    return True


text = input()

if halves_match(text):
    print("Match")
else:
    print("Do Not Match")