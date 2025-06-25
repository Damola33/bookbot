from stats import number_of_words, get_characters, sorted_count
import sys

def get_book_text(f_path):
    with open(f_path) as f:
        file_contents = f.read()
    return file_contents

def main():
    if len(sys.argv) != 2:
       print("Usage: python3 main.py <path_to_book>")
       sys.exit(1)
    path_to_book = sys.argv[1]
    book_text = get_book_text(path_to_book)
    num_words = number_of_words(book_text)
    num_chars = get_characters(book_text)
    sorted_chars = sorted_count(num_chars)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path_to_book}")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for dict in sorted_chars:
        if dict["char"].isalpha():
         print(f"{dict["char"]}: {dict["num"]}")


main()

