import time

# Open the file for reading
with open('panini_sutra.txt', 'r', encoding='utf-8') as file:
    # Read the contents of the file
    lines = file.readlines()

# Count the number of lines
line_count = len(lines)
print("Total lines in the file:", line_count)

# Iterate over the lines in batches of 1
for i, line in enumerate(lines, start=1):
    # Display the line number and the line content
    print(f"{i}. {line.rstrip()}")

    # Pause for 4 seconds
    time.sleep(1)

print("All lines displayed")
