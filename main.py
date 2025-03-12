from stats import count_words
from stats import count_characters
from stats import sort_character_counts

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
    frankenstein_character_counts = count_characters(frankenstein_contents)
    frankenstein_sorted_character_counts = sort_character_counts(frankenstein_character_counts)

    print(f"{frankenstein_word_count} words found in the document")
    print(frankenstein_sorted_character_counts)


main()