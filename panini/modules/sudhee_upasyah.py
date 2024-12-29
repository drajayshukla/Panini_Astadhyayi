
print('सुधी उपास्य: ')
input_string = 'सुद्ध्य् उप्आस्य्अ'
    #'सुधी उपास्य:'
    #input("Enter the input string: ")

# Split the input string into separate substrings
split_strings = input_string.split()
from separate_characters_list import separate_characters_and_map


output_string = separate_characters_and_map(split_strings)
print('characters separation:', output_string)
from switchoff.panini_tobe_developed.yanasandhi import replace_last_character

a = output_string
new_a = replace_last_character(a)
print('yana sandhi:',new_a)
from merging_in_list import merge_characters
word_list = new_a
merged_word = merge_characters(''.join(word_list))

print(merged_word)

