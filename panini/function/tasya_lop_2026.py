import re

def tasya_lop(input_list):
    """
    Removes everything inside curly brackets including the brackets
    from the strings in the input list.

    Parameters:
    input_list (list of str): List of strings to process

    Returns:
    list of str: Processed list with content inside {} removed
    """
    processed_list = []
    for item in input_list:
        # Remove everything inside curly brackets including the brackets
        processed_item = re.sub(r'\{.*?\}', '', item).strip()
        processed_list.append(processed_item)
    return processed_list

# Example usage
#input_strings = ['भ्अज्{अदित्}', '{घित्}अ{ञित्}']
#result = tasya_lop(input_strings)
#print("Final Output:", result)
