import re

def remove_curly_braces(input_list):
    """
    Removes curly braces '{}' from the strings in a list
    without altering the content inside them.
    """
    return [re.sub(r"[{}]", "", item) for item in input_list]

# Example usage
#example_list = ["{क}", "च", "{ज}", "झ", "{ञ}"]
#cleaned_list = remove_curly_braces(example_list)
#print(cleaned_list)  # Output: ['क', 'च', 'ज', 'झ', 'ञ']
