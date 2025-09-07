from relationship_app.models import Author, Book, Library, Librarian

# --- Sample Data Creation (Optional for Testing) ---
# Only run these once to avoid duplicates.
def create_sample_data():
    author = Author.objects.create(name="Jane Austen") 
    book1 = Book.objects.create(title="Pride and Prejudice", author=author)
    book2 = Book.objects.create(title="Sense and Sensibility", author=author)

    library = Library.objects.create(name="Central Library")
    library.books.add(book1, book2)

    librarian = Librarian.objects.create(name="Emily", library=library)

# --- Queries ---

# 1. Query all books by a specific author
def get_books_by_author(author_name):
    author = Author.objects.get(name=author_name) 
    return Book.objects.filter(author=author)        

# 2. List all books in a library
    def get_books_in_library(library_name):
        return Library.objects.get(name=library_name).books.all()

# 3. Retrieve the librarian for a library
def get_librarian_for_library(library_name):
    library = Library.objects.get(name=library_name)   
    return Librarian.objects.get(library=library)  
