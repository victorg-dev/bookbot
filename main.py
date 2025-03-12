from stats import count_words
from stats import count_characters
from stats import sort_character_counts

path_to_frankenstein = "books/frankenstein.txt"


# Opens a file and returns the entire contents
def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()

    return file_contents


# TODO write desc.
def generate_report(path_to_book, book_word_count, book_sorted_character_counts):
    report = "============ BOOKBOT ============\n"
    report += f"Analyzing book found at {path_to_book}\n"
    report += "----------- Word Count ----------\n"
    report += f"Found {book_word_count} total words\n"
    report += "--------- Character Count -------\n"
    for dict in book_sorted_character_counts:
        if dict["char"].isalpha():
            report += f"{dict["char"]}: {dict["count"]}\n"
    report += "============= END ==============="
        
    return report


def main():
    frankenstein_contents = get_book_text(path_to_frankenstein)
    frankenstein_word_count = count_words(frankenstein_contents)
    frankenstein_character_counts = count_characters(frankenstein_contents)
    frankenstein_sorted_character_counts = sort_character_counts(frankenstein_character_counts)

    frankenstein_report = generate_report(path_to_frankenstein, frankenstein_word_count, frankenstein_sorted_character_counts)
    print(frankenstein_report)


main()