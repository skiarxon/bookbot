from stats import get_word_count, get_character_counts, sorted_list
import sys

###read the contents of the file####
def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents


###does the other things#####
def main():
#    filepath = "books/frankenstein.txt"
    if len(sys.argv) > 1:  ###check for valid arguments
        filepath = sys.argv[1]
    else:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1) ### close with message
    book_text = get_book_text(filepath)
    book_word_count = get_word_count(book_text)
    lower_dictionary = get_character_counts(book_text)
    sorter = sorted_list(lower_dictionary)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}...")
    print("----------- Word Count ----------")
    print(f"Found {book_word_count} total words")
    print("--------- Character Count -------")
    for item in sorter:
        print(f"{item['char']}: {item['count']}")
    print("============= END ===============")

main()
