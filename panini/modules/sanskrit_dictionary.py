#this versio will remember all word serched
import csv
def find_matching_words(input_word):
    matching_words = []
    with open('dict_sanskrit.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            english_word = row[0].strip('"')
            if input_word.lower() in english_word.lower():
                matching_words.append(english_word)
    return matching_words

# Example usage
user_input = input("Enter an Sanskrit word(english): ")
matching_words = find_matching_words(user_input)
print("Matching words:")
for word in matching_words:
    print(word)

def find_word_meaning(input_word):
    with open('dict_sanskrit.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            english_word = row[0].strip('"')
            if english_word.lower() == input_word.lower():
                return row[2].strip('""')
    return "Meaning not found."


# Example usage
searched_words = []

# Load previously searched words from file
try:
    with open('searched_words_sans.txt', 'r') as file:
        searched_words = file.read().splitlines()
except FileNotFoundError:
    pass

while True:
    user_input = input("Enter an Sanskrit word (or ';;' to exit): ")
    if user_input == ";;":
        break

    meaning = find_word_meaning(user_input)
    if meaning:
        print(f"Meaning: {meaning}")
    else:
        print("Word not found.")

    searched_words.append(user_input)

# Store searched words in a text file
with open('searched_words_sans.txt', 'w') as file:
    for word in searched_words:
        file.write(word + '\n')
