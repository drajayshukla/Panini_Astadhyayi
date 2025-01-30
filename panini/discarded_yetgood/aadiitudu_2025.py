def replace_starting_characters_with_it(words):
    patterns_to_replace = ['ञ्इ', 'ट्उ', 'ड्उ']

    # If input is a single word (string), convert it to a list for uniform processing
    if isinstance(words, str):
        words = [words]

    modified_words = []
    for word in words:
        for pattern in patterns_to_replace:
            if word.startswith(pattern):
                word = '"इत्"' + word[len(pattern):]
                break
        modified_words.append(word)

    # Return a single word if input was a string, otherwise return the list
    return modified_words if len(modified_words) > 1 else modified_words[0]


# Example usage
#input_list = ['ञ्इकान', 'ट्उष', 'ड्उराज', 'अनमोल']
#modified_list = replace_starting_characters_with_it(input_list)
#print("Modified List:", modified_list)

#input_word = 'ञ्इकान'
#modified_word = replace_starting_characters_with_it(input_word)
#print("Modified Word:", modified_word)
