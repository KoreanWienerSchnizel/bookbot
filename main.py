def get_word_count(s):
    words = s.split()
    return len(words)

def get_char_freq_count(s):
    lower_text = s.lower()
    char_dict = {}
    for c in lower_text:
        if c not in char_dict:
            char_dict[c] = 0
        char_dict[c] += 1
    return char_dict

def sort_dict(char_dict):
    dict_list = char_dict.items()
    char_dict = dict(sorted(dict_list, key=lambda char_tuple: char_tuple[1], reverse=True)) 
    return char_dict

def print_book_report(file, word_count, char_dict):
    print(f"#######Report on {file}#######")
    print(f"{word_count} words found in the book \n")
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
