print('ट्ड्उभ्अज्अँ ड्उभ्अज्अँ षाकन् ल्युट् क्यच् आम्')
print('ञिमिदाँ श्यन् तिप् -here vriddhi is wrong')
print('मृजूँष् अनीयर्')
print('मृजूँष् शप् तिप् =मृजूँष् तिप् as per 2.4.72')
#'डुभजँ णघञ्'
# भजँ घञ्
#ट्ड्उभ्अज्अँ ड्उभ्अज्अँ षाकन्
input_string = input("Enter the input string: ")
   # 'डुभजँ घञ् षाकन् ण ल्युट् शप्'
    #'षाकन् ष्ट्रन् ष्वुन्  ष षच् षङ्गवच्  षिकन् षेण्यण् ष्कन् ष्टरच् ष्ठच् ष्ठन् ष्ठल् ष्फक् ष्यङ् ष्यञ् ष्फ '
    #'डुभजँ णघञ्'
    #

# Split the input string into separate substrings
split_strings = input_string.split()




from separate_characters_list_2025 import separate_characters_and_map


output_string = separate_characters_and_map(split_strings)
print('characters separation:', output_string)

from achanunasikit_2026 import replace_anunasik_with_respective_it, replace_anunasik_with_respective_it_in_list

# Example usage
words = output_string
modified_words = replace_anunasik_with_respective_it_in_list(words)
print('उपदेशेऽजनुनासिक इत्')
print('replace_anunasik_with_it(upadesh)',modified_words)
from halantayam_it_2026 import replace_last_hal_with_respective_it
word_3=replace_last_hal_with_respective_it(modified_words)
print('हलन्त्यम् ')
print('न विभक्तौ तुस्माः')
print('replace_last_hal_with_it(upadesh)',word_3)
from aadiitudu_2026 import replace_starting_characters_with_respective_it
word_4=replace_starting_characters_with_respective_it(word_3)

print('आदिर्ञिटुडवः(upadesh)',word_4)

from sha_pratyay_2026 import replace_starting_characters_with_it

# Define the path to the pratyaya file
pratyaya_file_path = '/Users/dr.ajayshukla/PycharmProjects/Panini_Astadhyayi/data/panini_function/pratyaya.txt'  # Update this path to the actual file location




# Input string


# Process the input string
word_5 = replace_starting_characters_with_it(word_4, pratyaya_file_path)

# Print the result
print('आदि:प्रत्यय :षः प्रत्ययस्य(pratyaya)', word_5)

from chutu_2026 import process_words

# Define the path to the pratyaya file
#/Users/dr.ajayshukla/PycharmProjects/Panini_Astadhyayi/data/panini_function
pratyaya_file_path = '/Users/dr.ajayshukla/PycharmProjects/Panini_Astadhyayi/data/panini_function/pratyaya.txt'  # Ensure this path points to the correct file location

# Define your input list

    #["चुटू", "ट्प्रयोग", "ड्उतक", "अनमोल", "प्रत्यय"]

# Process the words
word_6 = process_words(word_5, pratyaya_file_path)

# Print the results
print('replace_starting_chutu_with_it(pratyaya):', word_6)



from lashaku_ataddhite_2026 import process_words

# Define the path to the pratyaya file

pratyaya_file_path = '/Users/dr.ajayshukla/PycharmProjects/Panini_Astadhyayi/data/panini_function/taddhati_bhin_pratyaya.txt'  # Path to your .txt file
# Ensure this is the correct path

# Input list of words


# Process the words
word_7 = process_words(word_6, pratyaya_file_path)

# Print the results
print('check taddhati_bhin_pratyaya.txt')
print('lashaku_ataddhite(non taddhati pratyay:', word_7 )
from Lop_dict_2026 import generate_mapping

# Example usage

word_8_1 = generate_mapping(word_7)
print("Mapping of all it karya:", word_8_1)
from tasya_lop_2026 import tasya_lop
word_8 = tasya_lop(word_7)
print("tasya_lop:", word_8)
#from iko_gunvriddhi_113 import wrap_specific_vowels
#word_9=wrap_specific_vowels(word_8)
#print('इको गुणवृद्धी in {}:',word_9)
from mark_sangya_list import wrap_specific_vowels
word_9=wrap_specific_vowels(word_8)
print('इको गुणवृद्धी in {}:',word_9)

from anytxt_member import anytxt_member


# Specify the file path in your main code
#data_file_path = '/Users/dr.ajayshukla/PycharmProjects/Panini_Astadhyayi/data/panini_function/anga.txt'

# Example input list
#input_list = ['म्{इ}द्', 'य्अ', 'त्{इ}']

# Call the function with the specified file path
#word_10 = anytxt_member(word_9, data_file_path)

# Print the result
#print("Input:", input_list)
#print("identification of anga:", word_10)


from anga_random import anga_random
word_10 = anga_random(word_9)
for idx, pattern in enumerate(word_10, 1):
    print(f"Pattern_{idx}: {pattern}")
print("Pattern_selected:", word_10[0])
#import merging_in_list

#word_12 = merging_in_list.merge_characters(''.join(word_11))
#print('after Merging:',word_12 )
from vriddhi_replacement  import replace_in_brackets
word_11 = replace_in_brackets(word_10[0])
print(word_11)
from remove_brackets import replace_special_characters_flat
word_12=replace_special_characters_flat(word_11)
print(word_12)
from shutva_8236_enhanced import shutva_8236_final
word_12_1=shutva_8236_final(word_12)
print('shutva_8236:',word_12_1)
from remove_curly_bracket_inlist import remove_curly_braces
word_12_11=remove_curly_braces(word_12_1)
print(word_12_11)

import merging_in_list

word_13 = merging_in_list.merge_characters(''.join(word_12_11))
print('after Merging:',word_13 )



from word_to_python_list import word_to_list
word_13_1 = word_to_list(word_13)
print('python_list_after_merging:',word_13_1)

from separate_characters_list_2025 import separate_characters_and_map


word_14 = separate_characters_and_map(word_13_1)
print('characters separation:', word_14)
from shtuna_shtu_8441 import convert_shtrat_to_shtrat

word_15=convert_shtrat_to_shtrat(word_14)
print('ष्टुना ष्टुः-',word_15)

from merging_in_list_2026 import merge_characters

word_16 = merged_words = [merge_characters(word) for word in word_15]
print('after Merging:',word_16 )