# Original list
my_list = [
    "अः", "औ", "आः", "अम्", "औ", "आन्",
    "एन", "आभ्याम्", "ऐः", "आय", "आभ्याम्", "एभ्यः",
    "आत्", "आभ्याम्", "एभ्यः", "अस्य", "अयोः", "आनाम्",
    "ए", "अयोः", "एषु", "हे अ", "हे औ", "हे आः"
]

# Input word
base_word = "राम्"

# Create a new list by concatenating the base_word with each element in my_list
output_list = [base_word + item for item in my_list]

print(output_list)
