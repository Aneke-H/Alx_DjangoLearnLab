# 📘 Django Shell CRUD Operations: Book Model

This document summarizes all CRUD operations performed on the `Book` model using the Django shell.

---

## ✅ Create a Book Instance

**Command:**

```
from bookshelf.models import Book

book = Book.objects.create(
    title="1984",
    author="George Orwell",
    publication_year=1949
)

print(book)
```
Expected Output: **1984 created successfully***

*Confirms the book was successfully created in the database.*

🔍 Retrieve the Book Instance
Command:

```
from bookshelf.models import Book

book = Book.objects.get(title="1984")
print(book.title, book.author, book.publication_year)
```
Expected Output: **1984 George Orwell 1949**

*Retrieves and displays the full details of the book.*

✏️ Update the Book Title

```
from bookshelf.models import Book

book = Book.objects.get(title="1984")
book.title = "Nineteen Eighty-Four"
book.save()

print(book.title)
```


Expected Output:
**Nineteen Eighty-Four**
*The book's title is successfully updated and saved to the database.*

❌ Delete the Book Instance

```from bookshelf.models import Book

book = Book.objects.get(title="Nineteen Eighty-Four")
book.delete()
```

# Confirm deletion
```
books = Book.objects.all()
print(books)
```
Expected Output:
<QuerySet []>