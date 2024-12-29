import re

def find_unique_words(paragraph):
    # Remove punctuation marks and extra spaces
    clean_paragraph = re.sub(r'[^\w\s]', ' ', paragraph)

    # Split the paragraph into words and convert to lowercase
    words = clean_paragraph.lower().split()

    # Create a set of unique words
    unique_words = set(words)

    return unique_words

paragraph = ''''''

unique_words = find_unique_words(paragraph)
print(unique_words)
