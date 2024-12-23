import csv

def get_words_from_column(csv_file, column_index):
    words_list = []
    try:
        with open(csv_file, 'r', encoding='utf-8') as file:
            reader = csv.reader(file)
            for row in reader:
                if len(row) > column_index:  # Ensure the column index exists in the row
                    # Split the cell content into words and add to the list
                    words = row[column_index].split()
                    words_list.extend(words)
    except FileNotFoundError:
        print(f"The file {csv_file} does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")

    return words_list

# Example usage
csv_file_path = 'output.csv'  # Replace with your CSV file path
column_index = 3  # Replace with the column index you want to extract words from (0-based index)

words = get_words_from_column(csv_file_path, column_index)
print(f"Words from column {column_index}: {words}")
