from stats import get_char_freq_count, get_word_count, sort_dict


def print_book_report(file, word_count, char_dict):
    print(f"#######Report on {file}#######")
    print(f"{word_count} words found in the document \n")
    char_dict = sort_dict(char_dict)
    for c in char_dict:
        if c.isalpha():
            print(f"'{c}' was found {char_dict[c]} times")


def main():
    file = "books/frankenstein.txt"
    with open(file) as f:
        file_contents = f.read()
        word_count = get_word_count(file_contents)
        char_dict = get_char_freq_count(file_contents)
        print_book_report(file, word_count, char_dict)


if __name__ == "__main__":
    main()
