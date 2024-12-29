def generate_declensions(word):
    # Declensions for the word "गौरी" in different cases
    singular = {
        'nominative': word,  # गौरी
        'accusative': word[:-1] + 'ईम्',  # Corrected to गौरीम्
        'instrumental': word[:-1] + 'या',  # गौऱ्या
        'dative': word[:-1] + 'यै',  # गौऱ्यै
        'ablative': word[:-1] + 'याः',  # गौऱ्याः
        'genitive': word[:-1] + 'याः',  # गौऱ्याः
        'locative': word[:-1] + 'याम्',  # गौऱ्याम्
        'vocative': 'हे ' + word[:-1] + 'रि'  # हे गौऱि
    }

    dual = {
        'nominative': word[:-1] + 'यौ',  # गौऱ्यौ
        'accusative': word[:-1] + 'यौ',  # गौऱ्यौ
        'instrumental': word[:-1] + 'ीभ्याम्',  # गौऱीभ्याम्
        'dative': word[:-1] + 'ीभ्याम्',  # गौऱीभ्याम्
        'ablative': word[:-1] + 'ीभ्याम्',  # गौऱीभ्याम्
        'genitive': word[:-1] + 'योः',  # गौऱ्योः
        'locative': word[:-1] + 'योः',  # गौऱ्योः
        'vocative': 'हे ' + word[:-1] + 'यौ'  # हे गौऱ्यौ
    }

    plural = {
        'nominative': word[:-1] + 'यः',  # गौऱ्यः
        'accusative': word[:-1] + 'ईः',  # Corrected to गौरीः
        'instrumental': word[:-1] + 'ीभिः',  # गौऱीभिः
        'dative': word[:-1] + 'ीभ्यः',  # गौऱीभ्यः
        'ablative': word[:-1] + 'ीभ्यः',  # गौऱीभ्यः
        'genitive': word[:-1] + 'ीणाम्',  # गौऱीणाम्
        'locative': word[:-1] + 'ीषु',  # गौऱीषु
        'vocative': 'हे ' + word[:-1] + 'यः'  # हे गौऱ्यः
    }

    return singular, dual, plural


def print_declensions(declensions, number_name):
    print(f"\n{number_name} (वचनम्):")
    for case, form in declensions.items():
        print(f"{case.capitalize()}: {form}")


def main():
    word = "गौरी"
    singular, dual, plural = generate_declensions(word)

    print_declensions(singular, "Singular (एकवचनम्)")
    print_declensions(dual, "Dual (द्विवचनम्)")
    print_declensions(plural, "Plural (बहुवचनम्)")


if __name__ == "__main__":
    main()
