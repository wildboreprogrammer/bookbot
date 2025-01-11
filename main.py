def main(filepath_and_name):
    print(f"--- Begin report of books/{filepath_and_name} ---")
    with open(filepath_and_name) as f:
        book_string = f.read() #create string using entire file
        words = book_string.split() #create list of each word in book order splitting by white space
        character_count = {} #emtpy dictionary to contain character:charater count pairs.
        
        bookstring_list = list(book_string.lower()) #converts string to a list
        character_count_list = [] #list for sorting

        for i in range(0,len(bookstring_list)):
            if bookstring_list[i] in character_count and book_string[i].isalpha():
                character_count[bookstring_list[i]] += 1
                #print(character_count[bookstring_list[i]])
            elif bookstring_list[i].isalpha():
                character_count[bookstring_list[i]] = 1
        #print(character_count)

        character_count_list = list(character_count.items())
        character_count_list.sort(reverse=True, key=lambda a: a[1])
        
        print(f"{len(words)} words found in the document\n\n")
        for i in range(0,len(character_count_list)):
            print(f"The {character_count_list[i][0]} character was found {character_count_list[i][1]} times")
        print("--- End report ---")


main("books/frankenstein.txt")


""" Boot.dev's way of coding it for word count.

def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    print(text)


def get_book_text(path):
    with open(path) as f:
        return f.read()


main()

"""

""" Boot.dev's way of coding it for character count.
def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    print(f"{num_words} words found in the document")


def get_num_words(text):
    words = text.split()
    return len(words)


def get_book_text(path):
    with open(path) as f:
        return f.read()


main()
"""