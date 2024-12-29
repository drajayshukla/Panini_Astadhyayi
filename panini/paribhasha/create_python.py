import os
#this code take out those lines fron .txt which are starting from devanagari math numbers

def create_python_files_from_txt(txt_file):
    # Read the .txt file
    with open(txt_file, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    # Initialize variables
    current_name = None
    content = []
    base_dir = "output_files"  # Directory to store generated files

    # Create the base directory if it doesn't exist
    os.makedirs(base_dir, exist_ok=True)

    for line in lines:
        # Check if the line starts with a Devanagari digit
        if line.strip() and line[0] in "१२३४५६७८९०":
            # If there's a current_name, write its content to a file
            if current_name:
                file_path = os.path.join(base_dir, f"{current_name}.py")
                with open(file_path, 'w', encoding='utf-8') as py_file:
                    py_file.writelines(content)

            # Extract the name from the line
            current_name = line.strip().split(" ", 1)[-1].replace(" ", "_")  # Replace spaces with underscores
            content = []  # Reset content for the next file
        else:
            # Append lines to the current file's content
            content.append(line)

    # Write the last file if there's any content left
    if current_name:
        file_path = os.path.join(base_dir, f"{current_name}.py")
        with open(file_path, 'w', encoding='utf-8') as py_file:
            py_file.writelines(content)

    print(f"Python files generated in '{base_dir}' directory.")


# Specify the input .txt file
txt_file = "paribhasha_sutra.txt"  # Replace with the path to your .txt file
create_python_files_from_txt(txt_file)
