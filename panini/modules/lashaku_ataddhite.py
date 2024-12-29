def remove_starting_characters(word):
    patterns_to_remove =['क्', 'ख्', 'ग्', 'घ्', 'ङ्', 'ल्', 'श्']



    for pattern in patterns_to_remove:
        if word.startswith(pattern):
            word = word[len(pattern):]
            break
    return word


