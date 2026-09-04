def toggle_case(text):
    result = []

    # Write your traversal and transformation logic here
    for ch in text:
        if ch.isupper():
            result.append(ch.lower())
        elif ch.islower():
            result.append(ch.upper())
        else:
            result.append(ch)
    return "".join(result)


text = input()
print(toggle_case(text))