print('डुपचष् पाके=पचँष् लँट् ,पठँ लँट् ,भू लँट् ,यजँ लँट्')
print('डुभजँ घञ् षाकन्')
#'डुभजँ णघञ्'
#
input_string = 'डुभजँ घञ् षाकन् ण ल्युट् शप्'
    #'षाकन् ष्ट्रन् ष्वुन्  ष षच् षङ्गवच्  षिकन् षेण्यण् ष्कन् ष्टरच् ष्ठच् ष्ठन् ष्ठल् ष्फक् ष्यङ् ष्यञ् ष्फ '
    #'डुभजँ णघञ्'
    #input("Enter the input string: ")

# Split the input string into separate substrings
split_strings = input_string.split()




from separate_characters_list_2025 import separate_characters_and_map


output_string = separate_characters_and_map(split_strings)
print('characters separation:', output_string)

from achanunasikit_2025 import replace_anunasik_with_it, replace_anunasik_with_it_in_list

# Example usage
words = output_string
modified_words = replace_anunasik_with_it_in_list(words)
print('replace_anunasik_with_it(upadesh)',modified_words)
from halantayam_it import replace_last_hal_with_it
word_3=replace_last_hal_with_it(modified_words)
print('replace_last_hal_with_it(upadesh)',word_3)
from aadiitudu_2025 import replace_starting_characters_with_it
word_4=replace_starting_characters_with_it(word_3)
print('आदिर्ञिटुडवः(upadesh)',word_4)



from chutu_2025 import process_words

# Define the path to the pratyaya file
pratyaya_file_path = '/data/panini_function/pratyaya.txt'  # Ensure this path points to the correct file location

# Define your input list

    #["चुटू", "ट्प्रयोग", "ड्उतक", "अनमोल", "प्रत्यय"]

# Process the words
word_5 = process_words(word_4, pratyaya_file_path)

# Print the results
print('replace_starting_chutu_with_it(pratyaya):', word_5)
from sha_pratyay_2025 import replace_starting_characters_with_it

# Define the path to the pratyaya file
pratyaya_file_path = '/data/panini_function/pratyaya.txt'  # Update this path to the actual file location




# Input string


# Process the input string
word_6 = replace_starting_characters_with_it(word_5, pratyaya_file_path)

# Print the result
print('आदि:प्रत्यय :षः प्रत्ययस्य(pratyaya)', word_6)


from lashaku_ataddhite_2025 import process_words

# Define the path to the pratyaya file

pratyaya_file_path = '/data/panini_function/taddhati_bhin_pratyaya.txt'  # Path to your .txt file
# Ensure this is the correct path

# Input list of words


# Process the words
word_7 = process_words(word_6, pratyaya_file_path)

# Print the results
print('lashaku_ataddhite(non taddhati pratyay:', word_7 )
from tasya_lop_2025 import tasya_lop
word_8 = tasya_lop(word_7)
print("Final Output:", word_8)


