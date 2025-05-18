from stats import get_book_text, get_word_count, get_character_list, sort_dict, print_report

def main():
    frankenstein = "books/frankenstein.txt"
    file_contents = get_book_text(frankenstein)
    word_list = get_word_count(file_contents)
    char_dict = get_character_list(word_list)
    word_count = len(word_list)
    print_report(char_dict, frankenstein, word_count)

main()
