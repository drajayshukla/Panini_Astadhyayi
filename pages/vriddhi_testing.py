from panini.modules.vriddhi import get_vriddhi_vowels, identify_vriddhi_vowels, explain_vriddhi

# Example 1: Retrieve वृद्धि vowels
vriddhi_vowels = get_vriddhi_vowels()
print("वृद्धि vowels:", vriddhi_vowels)  # Output: ['आ', 'ऐ', 'औ']

# Example 2: Identify वृद्धि vowels in a string
input_string = "रामः शैवः गौरवः"
found_vowels = identify_vriddhi_vowels(input_string)
print("Found वृद्धि vowels:", found_vowels)  # Output: ['आ', 'ऐ', 'औ']

# Example 3: Explanation of वृद्धि संज्ञा
explanation = explain_vriddhi()
print(explanation)
