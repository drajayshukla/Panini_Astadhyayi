import os

def add_suffix_to_files(directory, suffix, extensions):
    """
    Adds a suffix to all files with specified extensions in a given directory.

    Parameters:
        directory (str): The path to the directory where files are located.
        suffix (str): The suffix to add to the file names.
        extensions (list): List of file extensions to target (e.g., ['.json', '.txt']).
    """
    # Iterate through files in the specified directory
    for filename in os.listdir(directory):
        # Check if the file has one of the specified extensions
        if any(filename.endswith(ext) for ext in extensions):
            # Construct the new file name
            base, ext = os.path.splitext(filename)
            new_name = f"{base}{suffix}{ext}"
            # Rename the file
            os.rename(os.path.join(directory, filename), os.path.join(directory, new_name))
            print(f"Renamed: {filename} -> {new_name}")

# Specify the directory (current directory in this case)
current_directory = os.getcwd()

# Specify the suffix and extensions
suffix_to_add = "_xyz"
file_extensions = ['.json', '.txt']

# Call the function
add_suffix_to_files(current_directory, suffix_to_add, file_extensions)
