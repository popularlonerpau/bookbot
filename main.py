from stats import num_of_words
from stats import num_of_characters
from stats import sorted_list

def get_book_text(book):
    with open(book) as f:
        return f.read()



def main():
    book = "books/frankenstein.txt"
    text = get_book_text(book)
    num = num_of_words(text)
    numchar = num_of_characters(text)
    newthing = sorted_list(numchar)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book}...")
    print("----------- Word Count ----------")
    print(f"Found {num} total words")
    print("--------- Character Count -------")
    for i in newthing:
        character = i["char"]
        number = i["num"]
        if not character.isalpha():
            continue
        print(f"{character}: {number}")
    print("============= END ===============")

main()
 
   