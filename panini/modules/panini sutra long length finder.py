input_file = "panini_sutra.txt"
output_file = "panini_output.txt"
specified_text = "योगप्रमाणे च तदभावेऽदर्शनं स्यात्"

with open(input_file, "r", encoding="utf-8") as file:
    lines = file.readlines()

selected_lines = [line for line in lines if len(line.strip()) > len(specified_text)]

with open(output_file, "w", encoding="utf-8") as file:
    file.writelines(selected_lines)
