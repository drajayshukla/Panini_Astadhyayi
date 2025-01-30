def tasya_lop(input_list):
    """
    Removes all occurrences of "इत्" from the strings in the input list
    and eliminates spaces caused by the removal.

    Parameters:
    input_list (list of str): List of strings to process

    Returns:
    list of str: Processed list with "इत्" removed
    """
    processed_list = []
    for item in input_list:
        # Remove all occurrences of "इत्" and any resulting spaces
        processed_item = item.replace('"इत्"', '').replace('  ', ' ').strip()
        processed_list.append(processed_item)
    return processed_list

# Example usage
#input_strings = [
    #'"इत्"भ्अज्"इत्"घ्अ',
    #'घ्अ"इत्"',
    #'"इत्"आक्अ"इत्"',
    #'"इत्"अ"इत्"',
    ###result = tasya_lop(input_strings)
#print("Final Output:", result)
