import time

# Open the file for reading
with open('panini_sutra.txt', 'r', encoding='utf-8') as file:
    # Read the contents of the file
    lines = file.readlines()

# Specify the minimum length for lines
min_length = len("पदान्तद्विर्वचनवरेयलोपस्वरसवर्णान")

# Ask the user to enter the line number to start from
start_line = int(input("Enter the line number to start from: "))

# Set the initial end line number
end_line = start_line + 4

# Iterate until the end of the document is reached
while start_line <= len(lines):
    # Iterate over the lines in the current batch
    for i, line in enumerate(lines[start_line-1:end_line], start=start_line):
        # Remove trailing newline character
        line = line.rstrip()

        # Check if the line is longer than the specified length
        if len(line) <= min_length:
            # Display the line number and the line content
            print(f"{i}. {line}")

    # Pause for 5 seconds
    time.sleep(5)

    # Update the start and end line numbers for the next batch
    start_line = end_line + 1
    end_line = start_line + 4

print("All lines displayed")
