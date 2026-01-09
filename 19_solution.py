from collections import Counter
import string

def count_word_frequency(file_path):
    try:
        with open(file_path, 'r') as file:
            text = file.read()

        translator = str.maketrans('', '', string.punctuation)
        text = text.translate(translator).lower()

        words = text.split()

        word_counts = Counter(words)

        sorted_word_counts = sorted(word_counts.items(), key=lambda x: (-x[1], x[0]))

        print("Word Frequency:")
        for word, count in sorted_word_counts:
            print(f"{word}: {count}")

    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

file_path = "Example.txt"  # Replace with your text file name
count_word_frequency(file_path)
