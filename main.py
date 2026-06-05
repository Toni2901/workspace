from stats2 import get_num_words, convert, sort_dict
import sys
def get_book_text(file_path):
    with open(file_path, encoding="utf-8-sig") as f:
        return f.read()

def main():
    if len(sys.argv) != 2:
        print(f"Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_path = sys.argv[1]
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    print(f"Found {num_words} total words")


    word_dict = convert(text)
    sorted_lst = sort_dict(word_dict)
    
    for item in sorted_lst:
        print(f"{item['char']}: {item['num']}")



main()

