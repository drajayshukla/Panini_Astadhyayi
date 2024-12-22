
a='अनँङ्'
from separate_characters import separate_characters_and_map, mapping


a = separate_characters_and_map(a)
print('Character separation',a)
from halantayam import remove_last_characters
a=remove_last_characters(a)
print('halantayam',a)
from anunasik_operations import remove_anunasik_akshar
a = remove_anunasik_akshar(a)

print('उपदेश :updeshe-ach anunasik it:', a)
