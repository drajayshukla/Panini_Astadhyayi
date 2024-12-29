import random
from difflib import SequenceMatcher

def calculate_similarity(text1, text2):
    """Calculate the similarity between two strings using SequenceMatcher."""
    return SequenceMatcher(None, text1, text2).ratio()

def extract_full_context(content, start_index, max_preceding_chars=100):
    """
    Extract text from up to 100 characters before the keyword to the next occurrence of either '],' or '": "'.
    """
    start = max(0, start_index - max_preceding_chars)
    context_start = content.rfind(": [", start, start_index)
    if context_start != -1:
        start = context_start

    end_comma = content.find("],", start_index)
    end_colon = content.find('": "', start_index)

    if end_comma == -1 and end_colon == -1:
        end = len(content)
    elif end_comma == -1:
        end = end_colon
    elif end_colon == -1:
        end = end_comma
    else:
        end = min(end_comma, end_colon)

    return content[start:end + 2]

def highlight_query_red(text, query):
    """Highlight occurrences of the query in the text with dark red text."""
    return text.replace(query, f"\033[31m{query}\033[0m")

def search_in_file(filepath, query, max_results=50):
    """
    Search for a keyword in the text file, avoiding repeated matches
    and those with >70% similarity to previous results.
    """
    try:
        with open(filepath, 'r', encoding='utf-8') as file:
            content = file.read()
    except FileNotFoundError:
        print("Error: File not found. Please check the file path.")
        return []

    results = []
    query_len = len(query)
    start = 0

    while True:
        start = content.find(query, start)
        if start == -1:
            break

        full_context = extract_full_context(content, start)

        # Avoid selecting matches >70% similar to already added results
        if any(calculate_similarity(full_context, result) > 0.7 for result in results):
            start += query_len
            continue

        highlighted_context = highlight_query_red(full_context, query)
        results.append(highlighted_context)

        start += query_len  # Move the search start index to avoid infinite loops

        # Stop searching if 100 matches are found
        if len(results) >= 100:
            break

    # Randomize results if more than max_results are found
    if len(results) > max_results:
        results = random.sample(results, max_results)

    return results

def append_results_to_file(output_filepath, query, results):
    """Append search results to a text file with the query in red."""
    try:
        with open(output_filepath, 'a', encoding='utf-8') as file:
            file.write(f"Query: {query}\n")
            for i, result in enumerate(results, 1):
                file.write(f"{query} {i}:\n{result}\n\n")
            file.write("=" * 50 + "\n\n")
    except IOError as e:
        print(f"Error writing to the file: {e}")

def write_summary(output_filepath, found_items, not_found_items):
    """Write the summary of found and not found items to the output file."""
    try:
        with open(output_filepath, 'a', encoding='utf-8') as file:
            file.write("=== Summary ===\n")
            file.write("Items Found:\n")
            for item in found_items:
                file.write(f"- {item}\n")
            file.write("\nItems Not Found:\n")
            for item in not_found_items:
                file.write(f"- {item}\n")
            file.write("=" * 50 + "\n")
    except IOError as e:
        print(f"Error writing summary to the file: {e}")

def main():
    print("=== Sanskrit Text Keyword Search Tool ===")

    filepath = "/Users/dr.ajayshukla/PycharmProjects/Panini_Astadhyayi/data/kosh/skd/skd.json"
    output_filepath = "/Users/dr.ajayshukla/PycharmProjects/Panini_Astadhyayi/अणादय.txt"

    found_items = []  # List of items found
    not_found_items = []  # List of items not found

    while True:
        queries = input("\nEnter the keywords to search, separated by commas (or type 'exit' to quit): ").strip()
        if queries.lower() == 'exit':
            print("Exiting the search tool. Writing summary to the file...")
            write_summary(output_filepath, found_items, not_found_items)
            print(f"Summary written to '{output_filepath}'. Goodbye!")
            break

        query_list = [query.lstrip() for query in queries.split(',') if query.lstrip()]

        for query in query_list:
            print(f"\nProcessing query: '{query}'")
            results = search_in_file(filepath, query, max_results=50)

            if results:
                print(f"\nFound {len(results)} result(s) for '{query}': (Random selection of up to 50 matches)")
                for i, context in enumerate(results, 1):
                    print(f"{query} {i}:\n{context}\n")
                append_results_to_file(output_filepath, query, results)
                found_items.append(query)
                print(f"Results for '{query}' appended to '{output_filepath}'.")
            else:
                print(f"No results found for '{query}'. Skipping...")
                not_found_items.append(query)

if __name__ == "__main__":
    main()
