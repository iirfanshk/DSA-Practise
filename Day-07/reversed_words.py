def reverse_words(sentence):
    words = sentence.split()
    result = []

    # Traverse the words from right to left
    for i in range(len(words)-1,-1,-1):
        result.append(words[i])
    return " ".join(result)


sentence = input()
print(reverse_words(sentence))