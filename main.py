import sys
from stats import count_words
from stats import count_characters
from stats import sort_character_counts


# Opens a file and returns the entire contents
def get_book_text(path_to_file):
    with open(path_to_file) as file:
        file_contents = file.read()

    return file_contents


# Generates and returns a report of the contents of the
# file path specified by the user
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


# The main function handles argument validation and displaying
# the book report to the user
def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    try:
        book_contents = get_book_text(sys.argv[1])
    except Exception as error: #filenotfound error
        print(f"{error}\nEnter a correct file path.")
        sys.exit(1)
    
    book_word_count = count_words(book_contents)
    book_character_counts = count_characters(book_contents)
    book_sorted_character_counts = sort_character_counts(book_character_counts)
    book_report = generate_report(sys.argv[1], book_word_count, book_sorted_character_counts)
    print(book_report)


main()