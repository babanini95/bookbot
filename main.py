from stats import count_words

def get_book_text(filepath):
    with open(filepath) as file:
        file_content = file.read()
    return file_content

def main():
    print(f"{count_words(get_book_text("books/frankenstein.txt"))} words found in the document")

if __name__ == "__main__":
    main()
    