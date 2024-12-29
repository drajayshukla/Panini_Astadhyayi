# Module for Sutra 7.1.94

def replace_last_occurrence(word, old_char, new_chars):
    """
    Replaces the last occurrence of old_char in the word with new_chars.

    Args:
        word (str): The input word.
        old_char (str): The character to be replaced.
        new_chars (str): The characters to replace the old_char with.

    Returns:
        str: Modified word with the last occurrence of old_char replaced by new_chars.
    """
    reversed_word = word[::-1]
    reversed_new_chars = new_chars[::-1]
    replaced_word = reversed_word.replace(old_char[::-1], reversed_new_chars, 1)
    return replaced_word[::-1]

def apply_sutra_7_1_94(cleaned_strings):
    """
    Applies the logic of Sutra 7.1.94 to modify the cleaned_strings list.

    Args:
        cleaned_strings (list): List of strings to process.

    Returns:
        list: Modified list of strings.
    """
    if len(cleaned_strings) > 1:
        second_word = cleaned_strings[1]
        if 'ऋ' in second_word:
            modified_second_word = replace_last_occurrence(second_word, 'ऋ', 'अन्')
            cleaned_strings[1] = modified_second_word

    print('7:1:94=ऋदुशनस्पुरुदंसो‌‌ऽनेहसां च=ऋदन्तशब्दानाम्, तथा उशनस्/पुरुदंसस्/अनेहस्-एतेषां शब्दानां असम्बुद्धौ सुँ-प्रत्यये परे अनङ् आदेशः भवति ।')
    print(' अनँङ् =अन्')
    print('अनेन सूत्रेण चतुर्ण्णाम् शब्दानाम् विषये प्रथमैकवचनस्य सुँ-प्रत्यये परे अनङ्-आदेशः विधीयते -')
    print('१. ऋकारान्तशब्दाः - यथा पितृ, मातृ, कर्तृ आदयः')
    print('२. "उशनस्" शब्दः (= शुक्राचार्यः)')
    print('३. "पुरुदंसस्" शब्दः (= मार्जारः)')
    print('४. "अनेहस्" शब्दः (= समयः)')
    print('अनङ्-आदेशे ङकारः इत्संज्ञकः अस्ति, नकारोत्तरः अकारः च उच्चारणार्थः अस्ति, अतः द्वयोः लोपः भवति , "अन्" इत्येव अवशिष्यते ।')
    print('तथा च, ङित्वात् "ङिच्च १.१.५३" इत्यनेन अयं अन्त्यादेशः भवति ।')
    print('प्रक्रियाः एताः -')
    print('१. पितृ + सुँ → पिता')
    print('२. कर्तृ + सुँ → कर्ता')
    print('३. उशनस् + सुँ → उशना')
    print('४. पुरुदंसस् + सुँ → पुरुदंसा')
    print('५. अनेहस् + सुँ → अनेहा')
    print('अनेन सूत्रेण निर्दिष्टः "अनङ्" आदेशः सम्बोधनैकवचनस्य सुँ-प्रत्यये परे न भवति ।')
    print('यथा - कर्तृ + सम्बोधन सुँ → कर्तः, उशनस् + सम्बोधन सुँ → उशनः')
    print('वार्त्तिकम् - उशनसः सम्बुद्धौ अपि पक्षे अनङ् इष्यते ।')
    return cleaned_strings

# Example Usage
if __name__ == "__main__":
    cleaned_strings = ["test", "पुरुदंसऋ"]  # Example list
    second_word = cleaned_strings[1]
    if 'ऋ' in second_word:
        modified_second_word = replace_last_occurrence(second_word, 'ऋ', 'अन्')
        cleaned_strings[1] = modified_second_word

    print('7:1:94=ऋदुशनस्पुरुदंसो‌‌ऽनेहसां च=ऋदन्तशब्दानाम्, तथा उशनस्/पुरुदंसस्/अनेहस्-एतेषां शब्दानां असम्बुद्धौ सुँ-प्रत्यये परे अनङ् आदेशः भवति ।')
    print(' अनँङ् =अन्')
    print('Modified Cleaned Strings:', cleaned_strings)
