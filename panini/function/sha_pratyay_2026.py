def load_pratyaya(file_path):
        """Load pratyayas from a text file into a list."""
        with open(file_path, 'r', encoding='utf-8') as file:
                pratyayas = [
                        line.strip() for line in file
                        if line.strip() and not line.startswith('#')  # Skip comments
                ]
        return pratyayas


def replace_starting_characters_with_it(words, pratyaya_file):
        """Replace starting 'ष्' with '"इत्"' for each word in the list, if the word is in the pratyaya file."""
        # Load pratyayas
        pratyayas = load_pratyaya(pratyaya_file)

        # Process each word individually
        modified_words = []
        for word in words:
                if any(word.startswith(pratyaya) for pratyaya in pratyayas):
                        if word.startswith('ष्'):
                                word = '{षित्}' + word[2:]  # Replace 'ष्' with '"इत्"'
                modified_words.append(word)
        return modified_words


def process_words(input_list, pratyaya_file):
        """Process a list of words to replace starting 'ष्' with '"इत्"' if they match the pratyaya file."""
        return [replace_starting_characters_with_it(word, pratyaya_file) for word in input_list]




# Example Usage
pratyaya_file_path = '/data/panini_function/pratyaya.txt'  # Update this path to the actual file location


