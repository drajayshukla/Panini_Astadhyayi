def remove_prefix(word, prefix):
    if word.startswith(prefix):
        return word[len(prefix):]
    return word

words = [
    "र्आम्अ:",
    "र्आम्औ",
    "र्आम्आ:",
    "र्आम्अम्",
    "र्आम्आन्",
    "र्आम्एण्अ",
    "र्आम्आभ्य्आम्",
    "र्आम्ऐ:",
    "र्आम्आय्अ",
    "र्आम्एभ्य्अ:",
    "र्आम्आत्",
    "र्आम्अस्य्अ",
    "र्आम्अय्ओ:",
    "र्आम्आण्आम्",
    "र्आम्ए",
    "र्आम्एष्उ"
]

prefix_to_remove = "र्आम्"
output_words = []

for word in words:
    output_word = remove_prefix(word, prefix_to_remove)
    output_words.append(output_word)

print(output_words)
