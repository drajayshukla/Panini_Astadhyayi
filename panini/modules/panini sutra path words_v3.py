import time

# Open the file for reading
with open('panini_sutra_2.txt', 'r', encoding='utf-8') as file:
    # Read the contents of the file
    lines = file.readlines()

# Count the number of lines
line_count = len(lines)
print("Total lines in the file:", line_count)

# Ask for user input to determine the starting line
start_line = int(input("Enter the line number to start from: "))

# Iterate over the lines starting from the specified line
for i in range(start_line-1, line_count):
    line = lines[i]
    # Display the line number and the line content
    print(f"{i+1}. {line.rstrip()}")

    # Pause for 1 second
    time.sleep(1)

print("All lines displayed")