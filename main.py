def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    print(text)
    words = text.split()
    print(count_words(words))


def get_book_text(path):
    with open(path) as f:
        return f.read()


def count_words(word_list):
    return len(word_list)

main()
