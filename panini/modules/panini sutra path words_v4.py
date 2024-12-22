import time

# Open the file for reading
with open('panini_sutra.txt', 'r', encoding='utf-8') as file:
    # Read the contents of the file
    lines = file.readlines()

# Specify the minimum length for lines
min_length = len("पदान्तद्विर्वचनवरेयलोपस्वरसवर्णान")

# Iterate over the lines in batches of 1
for i, line in enumerate(lines, start=1):
    # Remove trailing newline character
    line = line.rstrip()

    # Check if the line is longer than the specified length
    if len(line) > min_length:
        # Display the line number and the line content
        print(f"{i}. {line}")

        # Pause for 1 second
        time.sleep(3)

print("All lines displayed")
