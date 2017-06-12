# this is the blueprint for making books. A simple one, at least for now.
# according to this blueprint, a book only has three attributes or
# characteristics (title, author and pub_year). 
class Book(object):
    """A Book Object."""
    def __init__(self, title, author, pub_yr='Unknown'):
        self.title = title
        self.author = author
        self.pub_yr = pub_yr

    def __repr__(self):
        return '<Book. Title: %s.>' % (self.title)



class Library(object):
    """A collection of book objects."""

    def __init__(self):
        self.books = []

    def __repr__(self):
        return '<Library containing %s book(s).>' % (len(self.books))

    def list_books(self):
        """List all the books in the library."""

        if len(self.books) == 0:
            print "Library is empty."
            return
        for book in self.books:
            print book.title
            print '  Author:', book.author
            print '  Published:', book.pub_yr
            print

    def add_book(self, book):
        """Add a book to the library."""

        if not isinstance(book, Book):
            raise Exception('Please enter a Book Object to add to the library')
        self.books.append(book)
        print 'Added: %s' % (book.title)

    def empty_library(self):
        # assign an empty list '[]' to our library, it will dump
        # its contents and replace with the empty library
        self.books = []
        """Remove all books from the library."""


########### WRITE YOUR SCRIPT HERE
# Details on what the script should include are in the skills assessment 
# instructions.

def main():
    #PART 1:
    # the constructor "__init__" takes the arguments inside the parentheses
    # and builds the object from the blueprint
    book1 = Book("Bell Jar", "Sylvia Plath", "1963")
    book2 = Book("Anna Karenina", "Leo Tolstoy", "Unknown")


    # create a library
    lib = Library()


    # print all books in empty library
    lib.list_books()
    # print lib

    # add books to the created library 'lib'
    lib.add_book(book1)
    lib.add_book(book2)


    # list books again
    lib.list_books()
    # print lib

    
    #PART 2
    # the method under empty_library has been updated
    # now to verify that the books are empty
    lib.empty_library()
    
    lib.list_books() # these should be empty now


    #PART 3
    # updated add_book method
   
    
main()
