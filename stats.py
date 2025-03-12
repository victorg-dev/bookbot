# Takes book contents as a string and returns the number of words
def count_words(contents):
    words_list = contents.split() # split all whitespace
    return len(words_list)