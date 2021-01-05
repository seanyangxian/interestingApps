"""
Book collection manager.
Author: Xian Yang (Sean)
"""
import sys
import doctest


def openfile(file_name: str) -> tuple:
    """

    Read a text file and store each book's information into a dictionary, store all books into a tuple.

    :param file_name: a string representing the file name to be opened.
    :precondition: file name must be a string and represent file path in correct format
    :postcondition: return a tuple with all books information stored correctly.
    :return: a tuple that contains all books information stored in dictionaries.

    """
    filename = file_name
    stored_book = []
    try:
        with open(filename, encoding='utf-16') as file_object:
            format_openfile(stored_book, file_object)
        return tuple(stored_book)
    except FileNotFoundError:
        print('File not found.')


def format_openfile(stored_book: list, file_object) -> list:
    """

    Read a file object and store information of each line to dictionary format

    :param stored_book: a list to contain book information stored in dictionaries.
    :param file_object: a file object that contains all books information in text.
    :precondition: stored_book must be a list; file_object must be a txt file opened by using 'with open'
    :postcondition: return a tuple with all books information stored correctly.
    :return: a list that contains all books information stored in dictionaries.

    >>> test_book = open('test_Books_UTF_one_book.txt', encoding='utf-16')
    >>> format_openfile([], test_book)
    [{'Author': 'Lem', 'Title': 'Solaris', 'Publisher': 'BCIT', 'Shelf': '2', 'Category': 'Fiction', 'Subject': 'SF'}]

    >>> test_book = open('test_Books_UTF_empty.txt', encoding='utf-16')
    >>> format_openfile([], test_book)
    []

    """
    keys = file_object.readline().strip().split()
    for line in file_object:
        single_book_value = line.strip().split('\t')
        single_book = {}
        for i in range(len(keys)):
            if single_book_value[i] == '':
                single_book[keys[i]] = None
            else:
                single_book[keys[i]] = single_book_value[i]
        stored_book.append(single_book)
    return stored_book


def print_search_result(result_books: list):
    """

    Print search result in format

    :param result_books: a list which contains filtered book's dictionary
    :precondition: result_books must be a list which contains dictionaries.
    :postcondition: print all resulted books in correct format

    >>> test_book = [{'Author': 'Dupre', 'Title': 'Skyscrapers', 'Publisher': 'BD&L', 'Shelf': '12', \
    'Category': 'Architecture', 'Subject': '20th Century'}]
    >>> print_search_result(test_book)
    1 results match your need:
    -----------------------------------------
    1.
    Author: Dupre
    Title: Skyscrapers
    Publisher: BD&L
    Shelf: 12
    Category: Architecture
    Subject: 20th Century
    """
    print(f'{len(result_books)} results match your need:')
    for index, book in enumerate(result_books, 1):
        print('-----------------------------------------')
        print(f"{index}.")
        print(f"Author: {book['Author']}")
        print(f"Title: {book['Title']}")
        print(f"Publisher: {book['Publisher']}")
        print(f"Shelf: {book['Shelf']}")
        print(f"Category: {book['Category']}")
        print(f"Subject: {book['Subject']}")


def search_by(stored_books: tuple, key_word: str, by_option: str) -> list:
    """

    Search books by option based on provided key word; print out all results and number of results.

    :param stored_books: a tuple which contains all book's dictionary
    :param key_word: a string representing a key word piece of the search option
    :param by_option: a string representing the search option
    :precondition: key_word and by_option must be a string; stored_books must be a tuple
    :postcondition: print total number of books which match criteria and a numbered list of information of these books.
    :return: a list that contains all filtered books

    >>> test_books = openfile('test_Books_UTF_one_book.txt')
    >>> search_by(test_books,'em','1')
    1 results match your need:
    -----------------------------------------
    1.
    Author: Lem
    Title: Solaris
    Publisher: BCIT
    Shelf: 2
    Category: Fiction
    Subject: SF
    [{'Author': 'Lem', 'Title': 'Solaris', 'Publisher': 'BCIT', 'Shelf': '2', 'Category': 'Fiction', 'Subject': 'SF'}]
    """
    result_books = []
    for book in stored_books:
        try:
            if 0 < int(by_option) < len(book.keys()) + 1:
                book_value = book[list(book)[int(by_option) - 1]]
                if key_word.isnumeric() and book_value.isnumeric() and list(book)[int(by_option) - 1] == 'Shelf':
                    if int(key_word) == int(book_value):
                        result_books.append(book)
                elif key_word.lower() in book_value.lower():
                    result_books.append(book)
            else:
                print(f'Search option cannot must be positive integer up to {len(book)}, please try again.')
                return []
        except AttributeError:
            book[list(book)[int(by_option) - 1]] = ''
            if key_word == '':
                result_books.append(book)
                book[list(book)[int(by_option) - 1]] = None
    print_search_result(result_books)
    return result_books


def search(stored_books: tuple) -> list:
    """

    Ask what does the user want to search by and the search key word, then perform corresponding search.

    :param stored_books: a tuple which contains all of books' information stored in dictionaries.
    :precondition: stored_books must be a tuple which contains books stored in correct dictionary form;
                    user input must follow the instruction.
    :postcondition: perform corresponding type of search based on user's input.
    :return: a list that contains all filtered books

    """
    user_choice = input('Please choose the following option for what do you want to search by: \n1 = by author'
                        '\n2 = by title\n3 = by publisher\n4 = by shelf\n5 = by category\n6 = by subject\n').strip()
    try:
        search_keyword = input('Please enter the keyword you want to search: \n').strip()
        return search_by(stored_books, search_keyword, user_choice)
    except ValueError:
        print('Please choose a valid option for searching.')
        return []


def quit_book(stored_books: tuple):
    """

    Write modified books information to a new txt file and end the program.

    :param stored_books: a tuple which contains all of books' information stored in dictionaries.
    :precondition: stored_books must be a tuple which contains books stored in correct dictionary form;
                    filename must be a string in .txt format; user input must follow the instruction.
    :postcondition: write modified books information to a new txt file in correct format, then end the program

    """
    filename = 'new_books.txt'
    with open(filename, 'w', encoding='utf-16') as file_object:
        format_quit_book(stored_books, file_object)
        print(f"New books information has been writen to {filename} successfully.")
        print('End of program.')
        sys.exit()


def format_quit_book(stored_books: tuple, file_object):
    """

    Write modified books information to a new txt file in same format as the original file

    :param stored_books: a tuple which contains all of books' information stored in dictionaries.
    :param file_object: a file object that contains all books information in text.
    :precondition: stored_books must be a tuple which contains books stored in correct dictionary form;
    :postcondition: write modified books information to a new txt file, one book per line

    >>> test_new_book = open('test_new_books.txt', 'w', encoding='utf-16')
    >>> test_book = openfile('test_Books_UTF_one_book.txt')
    >>> format_quit_book(test_book, test_new_book)
    >>> test_new_book = open('test_new_books.txt', 'r', encoding='utf-16')
    >>> format_openfile([],test_new_book)
    [{'Author': 'Lem', 'Title': 'Solaris', 'Publisher': 'BCIT', 'Shelf': '2', 'Category': 'Fiction', 'Subject': 'SF'}]

    """
    if len(stored_books) > 0:
        file_object.write('\t'.join(stored_books[0].keys()))
        for book in stored_books:
            for key in book.keys():
                if not book[key]:
                    book[key] = ''
            file_object.write('\n' + '\t'.join(book.values()))


def move(stored_books: tuple, available_shelf: set):
    """

    Search for a book to move then move the book to desired destination

    :param stored_books: a tuple which contains all of books' information stored in dictionaries.
    :param available_shelf: a set which contains all available shelf in Chris's house.
    :precondition: stored_books must be a tuple which contains books stored in correct dictionary form;
                    user input must follow the instruction.
    :postcondition: move book_to_move to destination_shelf shelf correctly

    """
    print('Please search for the book you want to move:')
    books_to_move = search(stored_books)
    if len(books_to_move) == 0:
        print('There is no book to move, please search again.')
    else:
        index_to_move = input("Please choose which book you want to move: (enter the listed number of the book.)\n")
        try:
            if 0 < int(index_to_move) <= len(books_to_move):
                destination_shelf = input(
                    "Please tell me where do you want to move the book to? Please enter: the book shelf "
                    "numbers: 1 - 38, and one of 'Gaby', 'Island', 'Lego', 'Noguchi', 'Reading', "
                    "and 'Students'\n").strip().lower().capitalize()
                if destination_shelf in available_shelf:
                    books_to_move[int(index_to_move) - 1]['Shelf'] = destination_shelf
                    print(f'The book you have chosen has been moved to shelf {destination_shelf} successfully.')
                else:
                    print('Please enter a valid location.')
            else:
                print("The book index you entered is invalid, please try again.")
        except ValueError:
            print("The book index you entered is invalid, please try again.")


def get_valid_location(stored_books: tuple) -> set:
    """

    Create a set which contains all valid shelf number

    :precondition: no precondition, the function always executes successfully
    :postcondition: get all valid shelf number which a book can be moved to
    :return: a set that contains all valid shelf number

    >>> test_books = openfile('test_Books_UTF_three_books.txt')
    >>> get_valid_location(test_books)
    {'12', '6'}

    >>> test_books = openfile('test_Books_UTF_empty.txt')
    >>> get_valid_location(test_books)
    set()
    """
    valid_location = set()
    for book in stored_books:
        if book['Shelf'] is not None:
            valid_location.add(book['Shelf'])
    return valid_location


def menu(stored_books: tuple):
    """

    Display guidance information and ask user for input to perform corresponding action.

    :param stored_books: a tuple which contains all of books' information stored in dictionaries.
    :precondition: stored_books must be a tuple which contains books stored in correct dictionary form;
                    user input must follow the instruction.
    :postcondition: perform correct search or move based on user's input.

    """
    while True:
        user_choice = input('Hi, do you want to search books or move a book today?\n'
                            '1 = search\n2 = move\n3 = quit\n').strip().lower()
        if user_choice == '1':
            search(stored_books)
        elif user_choice == '2':
            move(stored_books, get_valid_location(stored_books))
        elif user_choice == '3':
            quit_book(stored_books)
        else:
            print("Please choose a valid option.")


def books():
    """

    Main function that run the whole program

    """
    my_books = openfile('Books UTF-16.txt')
    menu(my_books)


def main():
    """

    Drives the program.

    """
    books()
    doctest.testmod()


if __name__ == "__main__":
    main()
