input_file = "panini_sutra.txt"
output_file = "panini_sutra_2.txt"

with open(input_file, "r", encoding="utf-8") as file:
    lines = file.readlines()

output_lines = []
for line in lines:
    modified_line = ""
    for i in range(0, len(line), 10):
        modified_line += line[i:i+10] + "-"
    modified_line = modified_line[:-1]  # Remove the last hyphen
    output_lines.append(modified_line)

with open(output_file, "w", encoding="utf-8") as file:
    file.writelines(output_lines)
