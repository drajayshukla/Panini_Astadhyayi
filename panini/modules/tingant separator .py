
print('न्इन्द्')
input1 =input('enter words of tidant')
#input1 = "न्इन्द्"
input2 = "न्इन्द्अत्इ;न्इन्द्अत्ः;न्इन्द्अन्त्इ;न्इन्द्अस्इ;न्इन्द्अथ्ः;न्इन्द्अथ्अ;न्इन्द्आम्इ;न्इन्द्आव्ः;न्इन्द्आम्ः"
input_ashirling='ननिन्द्यात्;निन्द्यास्ताम्;निन्द्यासुः;निन्द्याः;निन्द्यास्तम्;निन्द्यास्त;निन्द्यासम्;निन्द्यास्व;निन्द्यास्म'

words = input2.split(';')  # Split the string into individual words

output = [word.replace(input1, '') for word in words]  # Remove the target word from each word

output_str = ';'.join(output)  # Join the modified words with ';'

print(output_str)

words = input2.split(';')  # Split the string into individual words

output = [word.replace(input1, '') for word in words]  # Remove the target word from each word

output_str = ';'.join(output)  # Join the modified words with ';'

print(output_str)
