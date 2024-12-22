from character_transformations import transform_characters
from character_mapping import mapping


while True:
    user_input = input("Enter characters (or ';;' to exit): ")
    if user_input == ";;":
        break

    transformed_word = ""
    i = 0
    while i < len(user_input):
        char = user_input[i]
        if i < len(user_input) - 1 and (char + user_input[i+1]) in mapping:
            transformed_word += mapping[char + user_input[i+1]]
            i += 2
        elif char in mapping:
            transformed_word += mapping[char]
            i += 1
        else:
            transformed_word += char
            i += 1

    print("Transformed word:", transformed_word)



