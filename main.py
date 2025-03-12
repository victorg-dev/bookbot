path_to_frankenstein = "./books/frankenstein.txt"

# Opens a file and returns the entire contents
def get_book_text(path_to_file):
    print(f"Opening file: {path_to_file}")
    with open(path_to_file) as f:
        file_contents = f.read()[:500] # TODO: remove [:500]

    return file_contents

def main():
    # store frankenstein contents
    frankenstein_contents = get_book_text(path_to_frankenstein)

    print(f"CONTENTS:\n{frankenstein_contents}")

main() # call main