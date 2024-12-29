import re
import json
from sklearn.feature_extraction.text import TfidfVectorizer
import numpy as np

def preprocess_text(text):
    """
    Preprocess the text by removing special characters and lowercasing.
    """
    text = re.sub(r'\s+', ' ', text)  # Replace multiple spaces with a single space
    return text.strip()

def custom_tokenize(content):
    """
    Tokenize Devanagari text into sentences using custom rules.
    """
    # Split by Devanagari punctuation marks
    sentences = re.split(r'[।॥]', content)
    # Remove empty strings and strip whitespace
    return [sentence.strip() for sentence in sentences if sentence.strip()]

def find_elaborative_sections(content, query, top_n=5):
    """
    Find text areas with the most elaborative discussion on the queried word or phrase.
    """
    # Tokenize content into sentences
    sentences = custom_tokenize(content)

    # Preprocess sentences and query
    sentences = [preprocess_text(sentence) for sentence in sentences]
    query = preprocess_text(query)

    # TF-IDF vectorization
    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform(sentences)
    query_vector = vectorizer.transform([query])

    # Compute relevance scores (cosine similarity)
    relevance_scores = (tfidf_matrix * query_vector.T).toarray().flatten()

    # Combine relevance and length scores for elaboration
    length_scores = np.array([len(sentence) for sentence in sentences])
    combined_scores = relevance_scores * (1 + np.log1p(length_scores))  # Weighted by length

    # Get the top N elaborative sections
    top_indices = np.argsort(combined_scores)[-top_n:][::-1]
    top_sentences = [(sentences[i], combined_scores[i]) for i in top_indices if combined_scores[i] > 0]

    return top_sentences

def main():
    # File path to the JSON file
    filepath = "/Users/dr.ajayshukla/PycharmProjects/Panini_Astadhyayi/data/kosh/skd/skd.json"  # Replace with your file path

    # Load the JSON content
    try:
        with open(filepath, 'r', encoding='utf-8') as file:
            data = json.load(file)  # Load the JSON data
    except FileNotFoundError:
        print("Error: File not found. Please check the file path.")
        return
    except json.JSONDecodeError:
        print("Error: Failed to decode JSON. Please check the file format.")
        return

    # Convert JSON to a single string of text
    if isinstance(data, dict):
        content = ' '.join([str(value) for value in data.values()])
    elif isinstance(data, list):
        content = ' '.join([str(item) for item in data])
    else:
        content = str(data)

    print("=== Sanskrit Text Elaborative Discussion Finder ===")
    while True:
        query = input("\nEnter the keyword or phrase to search (or type 'exit' to quit): ").strip()
        if query.lower() == 'exit':
            print("Exiting the tool. Goodbye!")
            break

        results = find_elaborative_sections(content, query, top_n=5)
        if results:
            print(f"\nTop {len(results)} elaborative sections on '{query}':")
            for i, (sentence, score) in enumerate(results, 1):
                highlighted_sentence = sentence.replace(query, f"\033[31m{query}\033[0m")
                print(f"\nResult {i} (Score: {score:.2f}):\n{highlighted_sentence}\n")
        else:
            print("No elaborative sections found. Try a different query.")


if __name__ == "__main__":
    main()
