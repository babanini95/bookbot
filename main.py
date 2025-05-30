from stats import count_words, count_char, sort_dict
import sys

def get_book_text(filepath: str) -> str:
    with open(filepath) as file:
        file_content = file.read()
    return file_content

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    text = get_book_text(sys.argv[1])
    char_dict = count_char(text)
    char_list = sort_dict(char_dict)
    print(f"============ BOOKBOT ============\nAnalyzing book found at {sys.argv[1]}")

    print(f"----------- Word Count ----------\nFound {count_words(text)} total words\n--------- Character Count -------")
    for char in char_list:
        print(f'{char["char"]}: {char["num"]}')
    print("============= END ===============")

if __name__ == "__main__":
    main()
    