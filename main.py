from stats import get_book_text, get_word_count, get_character_list, sort_dict, print_report
import sys

def argv_check(argv):
    if len(argv) < 2:
        raise Exception("Usage: python3 main.py <path_to_book>")

def main():
    book_name = sys.argv[1]
    file_contents = get_book_text(book_name)
    word_list = get_word_count(file_contents)
    char_dict = get_character_list(word_list)
    word_count = len(word_list)
    sorted_char_dict = sort_dict(char_dict)
    print_report(sorted_char_dict, book_name, word_count)

try:
    argv_check(sys.argv)
except Exception as e: 
    print(f"Error: {e}")
    sys.exit(1)

main()
