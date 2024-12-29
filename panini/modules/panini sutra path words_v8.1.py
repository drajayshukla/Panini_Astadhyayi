import time

# Open the file for reading
with open('panini_sutra.txt', 'r', encoding='utf-8') as file:
    # Read the contents of the file
    lines = file.readlines()

# Specify the minimum length for lines
min_length = len("पदान्तद्विर्वचनवरेयलोपस्वरसवर्णान")

# Ask the user to enter the line number to start from
start_line = int(input("Enter the line number to start from: "))

# Iterate over the lines starting from the specified line number
for i, line in enumerate(lines[start_line-1:], start=start_line):
    # Remove trailing newline character
    line = line.rstrip()

    # Check if the line is longer than the specified length
    if len(line) <= min_length:
        # Display the line number and the line content
        print(f"{i}. {line}")

        # Pause for 0.5 seconds
        time.sleep(1)

print("All lines displayed")
