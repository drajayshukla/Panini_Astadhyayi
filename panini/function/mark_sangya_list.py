from data.sangya_list  import pratyahara

def wrap_specific_vowels(input_list):
    """
    Wraps specific vowels in pratyahara["इक्"] with curly braces within strings in the input list.

    Args:
        input_list (list): A list of strings to process.

    Returns:
        list: A new list with the specified vowels wrapped in curly braces.
    """
    # Get the vowels from pratyahara["इक्"]
    vowels_to_wrap = {vowel: f"{{{vowel}}}" for vowel in pratyahara["इक्"]}

    # Process each string in the list
    wrapped_list = []
    for word in input_list:
        for vowel, wrapped in vowels_to_wrap.items():
            word = word.replace(vowel, wrapped)
        wrapped_list.append(word)

    return wrapped_list

# Example usage
# Define the pratyahara["इक्"] in sangya_list for this example:
# pratyahara = {"इक्": ["इ", "उ", "ऋ", "ऌ"]}

#example = ['म्इद्', 'य्अ', 'त्उ', 'ऋल']
#output = wrap_specific_vowels(example)
#print(output)
