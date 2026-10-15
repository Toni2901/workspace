from stats import *
import sys

def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()

def main():
    if len(sys.argv) != 2:
        print(f"Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_path = sys.argv[1]
    text = get_book_text(book_path)
    words = get_num_words(text)
    print(f"Found {words} total words")
 
    word_dict = convert(text)
    sort_lst = calibrate(word_dict)

    for item in sort_lst:
        print(f"{item["char"]}: {item["num"]}")

main()


        






































# from new_stats import *
# import sys

# def get_book_text(filepath):
#     with open(filepath) as f:
#         return f.read()

# def main():
#     if len(sys.argv) != 2:
#         print(f"Usage: python3 main.py <path_to_book>")
#         sys.exit(1)

#     book_path = sys.argv[1]
#     text = get_book_text(book_path)
#     words = get_num_words(text)
#     print(f"Found {words} words")


#     word_dict = convert(text)
#     sort_list = calibrate(word_dict)


#     for item in sort_list:
#         print(f"{item["char"]}: {item["num"]}")

# main()

