# Function to convert ष्त् to ष्ट् in a list of words
def convert_shtrat_to_shtrat(words):
    """
    Convert ष्त् to ष्ट् in each word of the given list.
    """
    return [word.replace("ष्त्", "ष्ट्") for word in words]

# Test input
#words = ['म्आर्ष्त्इ']
#converted_words = convert_shtrat_to_shtrat(words)
#print(converted_words)
