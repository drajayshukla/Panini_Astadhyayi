
print('पठ्,न्इन्द्')
input1 = input('enter dhatu in correct form:')
#input1 = "न्इन्द्"
input2 = "अत्इ;अतः;अन्त्इ;अस्इ;अथः;अथ्अ;आम्इ;आवः;आमः"

words = input2.split(';')  # Split the string into individual words

output = [input1 + word for word in words]  # Add the target word to each word

output_str = ';'.join(output)  # Join the modified words with ';'

print(output_str)

import re


def merge_characters(word):
        merged_word = word.replace("्ओ", "ो").replace("्औ", "ौ").replace("्आ", "ा").replace("्अ", "") \
                .replace('शइ', 'शि').replace('कउ', 'कु').replace('म्औ', 'मौ').replace('म्', 'म्') \
                .replace('म्ऐ', 'मै').replace('म्ए', 'मे').replace('त्', 'त्').replace('ष्उ', 'षु') \
                .replace('व्ए', 'वे').replace('व्ऐ', 'वै').replace('प्ऊ', 'पू').replace('त्ए', 'ते') \
                .replace('त्ऐ', 'तै').replace('न्इ', 'नि').replace('य्ए', 'ये').replace('र्इ', 'रि')\
                .replace('य्उ','यु').replace('क्ऋ','कृ').replace('त्इ','ति').replace('प्इ','पि')\
        .replace('ग्उ','गु').replace('द्ए','दे').replace('न्उ','नु')

        merged_word = re.sub(r'([इईउऊएऐऔअंअ:])्', r'\1', merged_word)

        # Handle case where ":" is not merged properly
        merged_word = re.sub(r'्:', ':', merged_word)

        return merged_word


# Example usage
#input_word =\
        #input("Enter a word: ")
result_11 = merge_characters(output_str)
print("कर्तरि लट्लकारः (परस्मैपदम्):", result_11)
