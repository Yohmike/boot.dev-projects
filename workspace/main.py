from typing import Callable

def open_book(filepath: str) -> Callable:
    with open(filepath) as f:
        return f.read()


def words_in_book(text: str) -> int:
    words = text.split()

    return len(words)

def main():
    book_path = "./books/frankenstein.txt"
    book_contents = open_book(book_path)
    print(words_in_book(book_contents))



if __name__ == "__main__":
    main()