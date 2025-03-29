from stats import get_num_words, get_char_counts

def get_book_text(filepath):
    try:
        with open(filepath, 'r') as file:
            return file.read()
    except FileNotFoundError:
        return f"Error: File not found at '{filepath}'"
    except Exception as e:
        return f"An error occurred: {e}"

def main():
    filepath = "books/frankenstein.txt"  # Ensure frankenstein.txt is in the same directory
    book_content = get_book_text(filepath)
    if isinstance(book_content, str) and not book_content.startswith("Error"):
        num_words = get_num_words(book_content)
        print(f"{num_words} words found in the document")

        char_counts = get_char_counts(book_content)
        print("Character Counts:")
        print(char_counts)
    else:
        print(book_content)

if __name__ == "__main__":
    main()
