import sys
from stats import get_num_words, get_num_char, chars_dict_to_sorted_list


def get_book_text(filepath):
    with open(filepath) as f:
        text = f.read()

        return text



def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    text = get_book_text(sys.argv[1])
    num_words = get_num_words(text)
    num_char = get_num_char(text)
    sorted_list = chars_dict_to_sorted_list(num_char)
    print_report(sys.argv[1],num_words, sorted_list)


def print_report(filepath, num_words, sorted_list):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    
    for item in sorted_list:
        ch = item["char"]
        if not ch.isalpha():
            continue
        print(f"{ch}: {item['num']}")
    
    print("============= END ===============")



main()





