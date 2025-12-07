def get_book_text(book):
    with open(book) as f:
        return f.read()


def num_of_words(text):
    dum = text.split()
    return dum



def main():
    book = "books/frankenstein.txt"
    text = get_book_text(book)
    num = num_of_words(text)
    print(text)
    print(f'Found {len(num)} total words')
    

    


main()

    
