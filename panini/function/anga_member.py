def anga_member(input_list):
    # Hard-coded file path
    file_path = '/Users/dr.ajayshukla/PycharmProjects/Panini_Astadhyayi/data/panini_function/anga.txt'

    # Read and split content from anga.txt into a list of lines
    with open(file_path, 'r', encoding='utf-8') as file:
        anga_contents = file.read().strip().splitlines()  # Split into a list of individual entries

    # Debugging print to check the list of anga contents
    print(f"Content list from anga.txt: {anga_contents}")

    # Process the input list
    output_list = [
        [item] if item in anga_contents else item
        for item in input_list
    ]
    return output_list

# Example usage
##print("Input:", input_list)
#output = anga_member(input_list)
#print("Output:", output)
