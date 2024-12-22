import random

# Components
karta_masculine = ['sah', 'balakah', 'raamah', 'narah']  # Masculine nouns
karta_feminine = ['saa', 'sitaa', 'gauri', 'balikaa']  # Feminine nouns
karta_neuter = ['tat', 'phalam', 'jalam', 'pushpam']  # Neuter nouns

# Verbs organized by gender and person
kriya_masculine = ['vadati', 'khadati', 'gachchhati', 'pashyati']
kriya_feminine = ['vadati', 'khadati', 'gachchhati', 'pashyati']  # Same as masculine for 3rd person singular
kriya_neuter = ['asti', 'bhavati', 'gachchhati', 'pashyati']  # Neuter verbs are context-specific

# Additional components
place = ['tatra', 'kutra', 'yatra', 'atra']
words = ['na', 'kim', 'nah', 'kah']
time = ['yada', 'sada', 'kada', 'naiv', 'tada', 'idani']
visheshan_masculine = ['svetah', 'peetah', 'subhrah', 'krishnah', 'haritah']
visheshan_feminine = ['svetaa', 'peetaa', 'subhraa', 'krishnaa', 'haritaa']
visheshan_neuter = ['svetam', 'peetam', 'subhram', 'krishnam', 'haritam']


# Function to generate sentences
def generate_sentence():
    # Randomly choose gender
    gender = random.choice(['masculine', 'feminine', 'neuter'])

    # Select nouns, verbs, and adjectives based on gender
    if gender == 'masculine':
        selected_karta = random.choice(karta_masculine)
        selected_kriya = random.choice(kriya_masculine)
        selected_visheshan = random.choice(visheshan_masculine)
    elif gender == 'feminine':
        selected_karta = random.choice(karta_feminine)
        selected_kriya = random.choice(kriya_feminine)
        selected_visheshan = random.choice(visheshan_feminine)
    else:  # neuter
        selected_karta = random.choice(karta_neuter)
        selected_kriya = random.choice(kriya_neuter)
        selected_visheshan = random.choice(visheshan_neuter)

    # Generate sentences
    sentences = [
        f"{selected_karta} {random.choice(place)} {selected_kriya}",
        f"{selected_karta} {random.choice(place)} {random.choice(words)} {selected_kriya}",
        f"{selected_karta} {random.choice(words)} {selected_kriya}",
        f"{random.choice(time)} {selected_karta} {random.choice(words)} {selected_kriya}",
        f"{selected_karta} {selected_visheshan} {selected_kriya}"
    ]
    return sentences


# Generate and print sentences
for _ in range(5):  # Generate 5 sentences
    for sentence in generate_sentence():
        print("Sentence:", sentence)
