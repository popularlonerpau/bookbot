from stats import num_of_words
from stats import num_of_characters

def get_book_text(book):
    with open(book) as f:
        return f.read()



def main():
    book = "books/frankenstein.txt"
    text = get_book_text(book)
    num = num_of_words(text)
    numchar = num_of_characters(text)
    return (text ,num ,numchar)

what, boy, girl = main()

#print(what)
print(f'Found {len(boy)} total words')
print(f'{girl}')
    

    


main()

    
