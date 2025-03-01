#Let's create a simple application to manage a library's catalog. This application will:
    #1 Store book information as tuples.
    #2 Add new books to the catalog.
    #3 Display all books in the catalog.
    #4 Search for books by author.

# List to store book information
library_catalog = [
    ("To Kill a Mockingbird", "Harper Lee", 1960),
    ("1984", "George Orwell", 1949),
    ("Pride and Prejudice", "Jane Austen", 1813),
    ("The Great Gatsby", "F. Scott Fitzgerald", 1925)
]

# Function to display all books in the catalog
def display_books():
    print("Library Catalog:")
    for title, author, year in library_catalog:
        print(f"Title: {title}, Author: {author}, Year: {year}")

# Displaying the books
display_books()

# Function to add a new book to the catalog
def add_book(title, author, year):
    new_book = (title, author, year)
    library_catalog.append(new_book)
    print(f"Book '{title}' by {author} added to the catalog.")

# Example usage
add_book("The Catcher in the Rye", "J.D. Salinger", 1951)

# Function to search for books by an author
def search_by_author(author):
    books_by_author = []
    for book in library_catalog:
        title, book_author, year = book
        if book_author.lower() == author.lower():
            books_by_author.append(book)
    return books_by_author

display_books()

# Example usage
books_by_orwell = search_by_author("George Orwell")
print("Books by George Orwell:")
for title, author, year in books_by_orwell:
    print(f"Title: {title}, Year: {year}")