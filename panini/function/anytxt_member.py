def anytxt_member(input_list, file_path):
    """
    Check items in the input list against entries in the specified file.

    Args:
        input_list (list): List of strings to process.
        file_path (str): Path to the file containing entries.

    Returns:
        list: Processed list where matching items are wrapped in a list.
    """
    # Read and split content from the file into a list of lines
    with open(file_path, 'r', encoding='utf-8') as file:
        anga_contents = file.read().strip().splitlines()  # Split into a list of individual entries

    # Debugging print to check the list of anga contents
    print(f"Content list from {file_path}: {anga_contents}")

    # Process the input list
    output_list = [
        [item] if item in anga_contents else item
        for item in input_list
    ]
    return output_list

'''from anytxt_member import anytxt_member


# Specify the file path in your main code
data_file_path = '/Users/dr.ajayshukla/PycharmProjects/Panini_Astadhyayi/data/panini_function/anga.txt'

# Example input list
#input_list = ['म्{इ}द्', 'य्अ', 'त्{इ}']

# Call the function with the specified file path
word_10 = anytxt_member(word_9, data_file_path)

# Print the result
#print("Input:", input_list)
print("Output:", word_10)'''