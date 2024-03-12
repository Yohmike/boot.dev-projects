from typing import Callable, Dict

def open_book(filepath: str) -> Callable:
    with open(filepath) as f:
        return f.read()


def words_in_book(text: str) -> int:
    words = text.split()
    return len(words)


def get_chars_from_text(text: str) -> Dict[str, int]:
    char_counts = {}
    for char in text:
        normalized_char = char.lower()
        char_counts[normalized_char] = char_counts.get(normalized_char, 0) + 1
    return char_counts

def build_report(filename: str, word_count: int, chars: Dict[str, int]):
    print(f"--- Report for book {filename} ---")
    print(f"\nThere are {word_count} words in the current book.\n")

    for key, value in sorted(chars.items(), key=lambda x: x[1], reverse=True):
        if key.isalnum():
            print(f"The {key} char appeared {value} times.")
    
    print("--- End report ---")


def main():
    book_path = "./books/frankenstein.txt"
    
    book_contents = open_book(book_path)
    
    words = words_in_book(book_contents)
    chars = get_chars_from_text(book_contents)
    
    build_report(book_path, words, chars)


if __name__ == "__main__":
    main()