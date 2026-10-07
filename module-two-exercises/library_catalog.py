class Book:
    def __init__(self, title, author, year):
        if not isinstance(year, int) or year <= 0:
            raise ValueError("Year must be positive integer")
        self.title = title
        self.author = author
        self.year = year
        self.checked_out = False

    def check_out(self):
        if self.checked_out:
            print(f"'{self.title}' is already checked out.")
        else:
            self.checked_out = True

    def return_book(self):
        self.checked_out = False

    def __repr__(self):
        status = "Checked Out" if self.checked_out else "Available"
        return f"{self.title} by {self.author} ({self.year}) - {status}"


class Ebook(Book):
    def __init__(self, title, author, year, file_size_mb):
        super().__init__(title, author, year)
        self.file_size_mb = file_size_mb
        self.checked_out = 0  # counter instead of boolean
    
    def check_out(self):
        self.checked_out += 1  # unlimited checkouts

    def return_book(self):
        if self.checked_out > 0:
            self.checked_out -= 1

    def __repr__(self):
        status = f"{self.checked_out} active checkouts"
        return (f"{self.title} by {self.author} ({self.year}) - "
                f"{status}, File size: {self.file_size_mb}MB")


class Catalog:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def search_by_author(self, author):
        return [b for b in self.books if b.author.lower() == author.lower()]

    def search_by_title(self, keyword):
        keyword = keyword.lower()
        return [b for b in self.books if keyword in b.title.lower()]

    def get_available(self):
        available = []
        for b in self.books:
            if isinstance(b, Ebook):  # Ebooks are always available
                available.append(b)
            else:
                if not b.checked_out:
                    available.append(b)
        return available

    def summary(self):
        print("\nCatalog Summary:")
        print("-" * 40)
        for b in self.books:
            print(b)
        print("-" * 40)


catalog = Catalog()

# Add books
catalog.add_book(Book("Python Crash Course", "Eric Matthes", 2019))
catalog.add_book(Book("Clean Code", "Robert Martin", 2008))
catalog.add_book(Ebook("AI Engineering", "Chip Huyen", 2025, 15.2))

# Search by title
results = catalog.search_by_title("python")
print("Search results:", results)

# Check out first physical book
catalog.books[0].check_out()

# Get available books
available = catalog.get_available()
print(f"Available books: {len(available)}")

# Summary of catalog
catalog.summary()

# Test Ebook checkout behavior
ebook = catalog.books[2]
ebook.check_out()
ebook.check_out()
print("After multiple ebook checkouts:", ebook)

# Return ebook once
ebook.return_book()
print("After returning ebook once:", ebook)

# Return physical book
catalog.books[0].return_book()
print("After returning physical book:", catalog.books[0])
                 
