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
    char_dict = dict(
        sorted(dict_list, key=lambda char_tuple: char_tuple[1], reverse=True)
    )
    return char_dict
