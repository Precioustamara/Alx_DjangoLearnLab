from .models import Book

***command for create**
Book.objects.create():
book = Book.objects.create(title = “1984”, author = “George Orwell”, publication_year = 1949)

#Expected Output
Successfully added
