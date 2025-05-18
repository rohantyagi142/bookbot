def get_book_text(fp):
    with open(fp) as f:
        file_contents = f.read()
    return file_contents

def get_word_count(file_contents):
    word_list = file_contents.split()
    return word_list

def get_character_list(word_list):
    
    char_dict = {}

    for word in word_list:
        word = word.lower()

        for i in range(0,len(word)):
            if word[i] in char_dict:
                char_dict[word[i]] += 1
            else:
                char_dict[word[i]] = 1

    return char_dict

def sort_dict(char_dict):
    char_list = []
    entry_dict = {}

    for character in char_dict:
        entry_dict["char"] = character
        entry_dict["num"] = char_dict[character]

        char_list.append(entry_dict)

        del entry_dict["char"]
        del entry_dict["num"]

    return char_list

def print_report(sorted_char_dict, fp, word_count):

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {fp}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")


    for entry_dict in sorted_char_dict:
        #entry_char = entry_dict["char"]
        #entry_num = entry_dict["num"]
        print(entry_dict)
        #print(f"'{entry_char}': {entry_num}")

    print("============= END ===============")
