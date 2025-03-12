# Takes book contents as a string and returns the number of words
def count_words(contents):
    words_list = contents.split() # split all whitespace
    return len(words_list)


# Takes book contents as a string and returns a dictionary of all
# the unique characters in the book and their respective counts
def count_characters(contents):
    contents = contents.lower()
    character_counts = {}
    for char in contents:
        if char in character_counts:
            character_counts[char] += 1
        else: # not in dict
            character_counts[char] = 1

    return character_counts


# Helper function which returns the value that should be used
# for sorting
def sort_by(dict):
    return dict["count"]


# TODO write desc.
def sort_character_counts(character_counts):
    sorted_character_counts = []
    for char, count in character_counts.items():
        sorted_character_counts.append({"char": char, "count": count})
    
    sorted_character_counts.sort(reverse=True, key=sort_by)

    return sorted_character_counts