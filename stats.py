def get_num_words(text):
    count = text.split()

    return len(count)


def get_num_char(text):
    num_char = {}

    lower_text = text.lower()

    for char in lower_text:
        if char in num_char:
            num_char[char] += 1
        else:
            num_char[char] = 1 

    return num_char


def sort_on(items):
    return items["num"]

def chars_dict_to_sorted_list(num_chars_dict):
    sorted_list = []
    for char in num_chars_dict:
        small_dict = {"char": char, "num": num_chars_dict[char]}
        sorted_list.append(small_dict)

    sorted_list.sort(key=sort_on, reverse=True)

    return sorted_list






