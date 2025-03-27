###get the count of the words in the text###
def get_word_count(book_text):
    book_words = book_text.split() ##split words 
    book_word_count = len(book_words)
    return book_word_count


###count all the characters###
def get_character_counts(book_text):
    to_lowercase_dict = {}
    for char in book_text:
        lower = char.lower() ###convert to lowercase
        if lower in to_lowercase_dict:
            to_lowercase_dict[lower] += 1
        else:
            to_lowercase_dict[lower] = 1
    return to_lowercase_dict

###show character and number of times found###
def sorted_list(to_lowercase_dict):
    character_list = []
    for char, count in to_lowercase_dict.items():
        if char.isalpha(): ###ignore symbols###
            character_list.append({"char": char, "count": count})
    character_list.sort(key=lambda item: item["count"], reverse=True)
    return character_list
