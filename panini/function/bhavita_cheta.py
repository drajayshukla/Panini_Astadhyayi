
print('भू तृच्  ,तॄ तृच् ')
input_string = input("Enter the input string: ")

# Split the input string into separate substrings
split_strings = input_string.split()

# Insert 'इट्' as a new list item
split_strings.insert(1, 'इट्')

print("Modified List:", split_strings)


from separate_characters_list_2025 import separate_characters_and_map


output_string = separate_characters_and_map(split_strings)
print('characters separation:', output_string)

from halantayam_list_best import remove_last_characters



modified_list = remove_last_characters(output_string)

print("Cleaned Strings(halantayam):", modified_list)
cleaned_strings=modified_list
from adengaguna import modify_cleaned_strings
modify_cleaned_strings(cleaned_strings)
print('7:1:84=सार्वधातुक-आर्धधातुकयोः=सार्वधातुके आर्धधातुके च प्रत्यये परे इगन्तस्य अङ्गस्य गुणादेशः भवति ')
print("Modified Cleaned Strings:", cleaned_strings)
print('6:1:78=एचोऽयवायावः')
from ayadi_list import modify_cleaned_strings

modified_cleaned_strings = modify_cleaned_strings(cleaned_strings)
print("Modified Cleaned Strings:", modified_cleaned_strings)

from list_merger import merge_strings
merged_string = merge_strings(modified_cleaned_strings[0], modified_cleaned_strings[1])
a=merged_string,modified_cleaned_strings[2]
print("Merged String:", a)


list_a = list(a)
print("Tuple converted to a list:", list_a)
cleaned_strings=list_a
cleaned_strings.append("स्")
print('1:2:46=कृत्तद्धितसमासाश्च')
print('''कृत्-प्रत्ययान्तशब्दानाम्, तद्धितप्रत्ययान्तशब्दानाम् तथा सामासिकशब्दानाम् 'प्रातिपदिकम्' इति संज्ञा भवति ''')
print(' सुँ = स्')
print("Modified Cleaned Strings:", cleaned_strings)
def replace_last_occurrence(word, old_char, new_chars):
    reversed_word = word[::-1]
    reversed_new_chars = new_chars[::-1]
    replaced_word = reversed_word.replace(old_char[::-1], reversed_new_chars, 1)
    return replaced_word[::-1]

second_word = cleaned_strings[1]
if 'ऋ' in second_word:
    modified_second_word = replace_last_occurrence(second_word, 'ऋ', 'अन्')
    cleaned_strings[1] = modified_second_word
print('7:1:94=ऋदुशनस्पुरुदंसोऽनेहसां च=ऋदन्तशब्दानाम्, तथा उशनस्/पुरुदंसस्/अनेहस्-एतेषां शब्दानां असम्बुद्धौ सुँ-प्रत्यये परे अनङ् आदेशः भवति ।')
print(' अनँङ् =अन्')
print("Modified Cleaned Strings:",cleaned_strings)

print('''पदच्छेदः  अप्-तृन्-तृच्-स्वसृ-नप्तृ-नेष्टृ-त्वष्टृ-क्षत्तृ-होतृ-पोतृ-प्रशास्तॄणाम् ( षष्ठी-बहुवचनम् )
अनुवृत्तिः  दीर्घः ६.३.१११ , उपधायाः ६.४.७ , न ६.४.७ , सर्वनामस्थाने ६.४.८ , च ६.४.८ , असम्बुद्धौ ६.४.८
अधिकारः  अङ्गस्य ६.४.१
अनुवृत्तिसहितं सूत्रम्  अप्-तृन्-तृच्-स्वसृ-नप्तृ-नेष्टृ-त्वष्टृ-क्षत्तृ-होतृ-पोतृ-प्रशास्तॄणामङ्गस्य उपधायाः असम्बुद्धौ सर्वनामस्थाने दीर्घः''')

print('''तृन्-प्रत्ययान्तशब्दाः, तृच्-प्रत्ययान्तशब्दाः, तथा अप्, स्वसृ, नप्तृ, नेष्टृ, त्वष्टृ, क्षत्तृ, होतृ, पोतृ, तथा 
प्रशातृ - एतेषामङ्गस्य उपधायाः असम्बुद्धिवाचके सर्वनामस्थानपरे दीर्घः भवति ।''')
print('''The उपधा letter of the words अप्, स्वसृ, नप्तृ, नेष्टृ, त्वष्टृ, क्षत्तृ, होतृ, पोतृ, 
and प्रशातृ, and also of the words ending in a तृन् or तृच् प्रत्यय becomes दीर्घ in presence of 
a प्रत्यय that is also a सर्वनामस्थान, other than सम्बोधन-एकवचन.''')

from upadha_deergh import apply_last_character_rules
cleaned_strings[1] = apply_last_character_rules(cleaned_strings[1])
print(cleaned_strings)
print('1:2:41=अपृक्त एकाल् प्रत्ययः:A प्रत्ययः that contains only one letter is called अपृक्त')
print('6:1:68=हल्ङ्याब्भ्यो दीर्घात् सुतिस्यपृक्तं हल् =हलन्तात्, दीर्घात् ङ्यन्तात्, दीर्घात् आबन्तात् च परस्य सुँ-ति-सि-प्रत्ययानाम् अपृक्तः हल् लुप्यते ।')
print('''The सुँ, ति, or सि प्रत्यय, when present as a single letter, 
is removed when attached to - (1) a word ending in a हल् letter, or
 (2) A दीर्घ word ending in the ङीप् / ङीष् / ङीन् / चाप् / टाप् / डाप् प्रत्यय.''')
cleaned_strings = cleaned_strings[:-1]
print('अपृक्त एकाल् प्रत्ययः,लोप :',cleaned_strings)

import merging_in_list

merged_word = merging_in_list.merge_characters(''.join(cleaned_strings))

print('8:2:7=नलोपः प्रातिपदिकान्तस्य :',merged_word)
print('The terminal न् letter of a प्रातिपदिक is omitted if the प्रातिपदिक also gets the पदसंंज्ञा')
from nalop_pratipadak import remove_last_character_if_needed

input = merged_word
output = remove_last_character_if_needed(input)

print(output)  # Output: चेता
