
print('जि लँट् ,णीञ् प्रापणे= नी लँट् ,भू लँट् ,तॄ लँट् ,डुपचँष् पाके=पचँष् लँट्  ')
input_string = input("Enter the input string: ")

# Split the input string into separate substrings
split_strings = input_string.split()




from separate_characters_list import separate_characters_and_map


output_string = separate_characters_and_map(split_strings)
print('characters separation:', output_string)

from halantayam_list_1 import remove_last_characters



modified_list = remove_last_characters(output_string)

print("Cleaned Strings(halantayam):", modified_list)
cleaned_strings=modified_list

from anunasik import remove_anunasik_akshar_from_list
#input_list = ['ज्इ', 'अ', 'ल्अँ']
output_list = remove_anunasik_akshar_from_list(cleaned_strings)
#print("Input:", input_list)
print("ach anunasik:", output_list)
print('तिप्=ति')
#a = ['ज्इ', 'ल्']
replacement_word = 'ति'
modified_list = [word.replace('ल्', replacement_word) for word in output_list]
print("Modified List:", modified_list)

# Insert 'इट्' as a new list item

modified_list.insert(1, 'अ')
print('शप्=अ')

print("Modified List:", modified_list)
from adengaguna import modify_cleaned_strings
modify_cleaned_strings(modified_list)
print('7:1:84=सार्वधातुक-आर्धधातुकयोः=सार्वधातुके आर्धधातुके च प्रत्यये परे इगन्तस्य अङ्गस्य गुणादेशः भवति ')
print("Modified Cleaned Strings:", modified_list)
print('6:1:78=एचोऽयवायावः')
from ayadi_list import modify_cleaned_strings

modified_cleaned_strings = modify_cleaned_strings(modified_list)
print("Modified Cleaned Strings:", modified_cleaned_strings)
import merging_in_list

merged_word = merging_in_list.merge_characters(''.join(modified_cleaned_strings))

print('merging:',merged_word)