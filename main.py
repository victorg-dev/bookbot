from stats import count_words

path_to_frankenstein = "./books/frankenstein.txt"

# Opens a file and returns the entire contents
def get_book_text(path_to_file):
    print(f"Opening file: {path_to_file}")
    with open(path_to_file) as f:
        file_contents = f.read()

    return file_contents


def main():
    frankenstein_contents = get_book_text(path_to_frankenstein)
    frankenstein_word_count = count_words(frankenstein_contents)

    print(f"{frankenstein_word_count} words found in the document")


main()