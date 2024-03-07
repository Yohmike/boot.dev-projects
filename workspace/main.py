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


def main():
    book_path = "./books/frankenstein.txt"
    book_contents = open_book(book_path)
    print(words_in_book(book_contents))
    chars = get_chars_from_text(book_contents)
    print(chars)


if __name__ == "__main__":
    main()