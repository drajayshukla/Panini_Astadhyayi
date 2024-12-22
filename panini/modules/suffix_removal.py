import os

def remove_suffix_from_files(directory, suffix, extensions):
    """
    Removes a specified suffix from file names in a given directory.

    Parameters:
        directory (str): The path to the directory where files are located.
        suffix (str): The suffix to remove from file names.
        extensions (list): List of file extensions to target (e.g., ['.txt', '.json']).
    """
    for filename in os.listdir(directory):
        # Check if the file has one of the specified extensions and the suffix
        if any(filename.endswith(ext) for ext in extensions) and suffix in filename:
            # Construct the new file name
            base, ext = os.path.splitext(filename)
            if base.endswith(suffix):
                new_base = base[:-len(suffix)]
                new_name = f"{new_base}{ext}"
                # Rename the file
                os.rename(os.path.join(directory, filename), os.path.join(directory, new_name))
                print(f"Renamed: {filename} -> {new_name}")

# Specify the directory (current directory in this case)
current_directory = os.getcwd()

# Specify the suffix and extensions
suffix_to_remove = "_xyz"
file_extensions = ['.txt', '.json']

# Call the function
remove_suffix_from_files(current_directory, suffix_to_remove, file_extensions)
