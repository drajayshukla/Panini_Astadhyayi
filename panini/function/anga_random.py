def anga_random(input_list):
    """
    Generates a list of patterns by marking items in brackets except the last item.

    Args:
        input_list (list): A list of strings to process.

    Returns:
        list: A list of generated patterns.
    """
    patterns = []

    # Generate patterns by grouping the first n items into a list, leaving the rest unmarked
    for i in range(1, len(input_list)):
        # Create the grouped pattern
        grouped = [input_list[:i]] + input_list[i:]
        patterns.append(grouped)

    return patterns

# Example usage
#example = ['म्इद्', 'य्अ', 'त्इ', 'क्अ']
#output = anga_random(example)
#for idx, pattern in enumerate(output, 1):
  #  print(f"Pattern_{idx}: {pattern}")
#print("Pattern_2:", output[1])