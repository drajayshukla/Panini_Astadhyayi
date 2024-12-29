import time

# Open the file for reading
with open('panini_sutra.txt', 'r', encoding='utf-8') as file:
    # Read the contents of the file
    lines = file.readlines()

# Iterate over the lines in batches of 10
batch_size = 1

for i in range(0, len(lines), batch_size):
    # Get the current batch of lines
    batch = lines[i:i+batch_size]

    # Display the current batch
    for line in batch:
        print(line.rstrip())  # Remove trailing newline character

    print()  # Add an empty line between batches

    # Pause for 6 seconds
    time.sleep(1)

print("All lines displayed")
