# Step 1: Creating your first class
class Book:
    """
    Book class represents a book in the library.
    This is our first class - a blueprint for creating book objects.
    """
    
    # Class variable (shared by all instances)
    total_books = 0
    
    # Constructor method - called when creating a new Book object
    def __init__(self, title, author, isbn):
        """
        Constructor that initializes a new Book object.
        
        Parameters:
        - title: The title of the book
        - author: The author of the book
        - isbn: Unique ISBN number
        """
        # Instance variables (unique to each book)
        self.title = title
        self.author = author
        self.isbn = isbn
        self.availability = True  # True = available, False = borrowed
        
        # Increment total books count
        Book.total_books += 1
        
        print(f"Book created: '{self.title}' by {self.author}")
    
    # Instance method - needs 'self' to access instance data
    def get_info(self):
        """Returns formatted information about the book"""
        status = "Available" if self.availability else "Borrowed"
        return f"'{self.title}' by {self.author} (ISBN: {self.isbn}) - {status}"
    
    # Another instance method
    def toggle_availability(self):
        """Toggles the availability status of the book"""
        self.availability = not self.availability
        status = "available" if self.availability else "borrowed"
        print(f"'{self.title}' is now {status}")
    
    # Class method - works with class variables
    @classmethod
    def get_total_books(cls):
        """Returns the total number of books created"""
        return cls.total_books
    
    # Static method - utility function that doesn't need self or cls
    @staticmethod
    def validate_isbn(isbn):
        """
        Validates ISBN format (simple validation).
        Returns True if valid, False otherwise.
        """
        # Simple ISBN validation: 10 or 13 digits
        clean_isbn = isbn.replace("-", "").replace(" ", "")
        return clean_isbn.isdigit() and len(clean_isbn) in [10, 13]
    
    # String representation of the object
    def __str__(self):
        """Returns a string representation of the Book"""
        return self.get_info()
    
    # Equality comparison
    def __eq__(self, other):
        """Books are equal if they have the same ISBN"""
        if isinstance(other, Book):
            return self.isbn == other.isbn
        return False
    
    # Convert book to dictionary (useful for JSON storage)
    def to_dict(self):
        """Converts Book object to dictionary for JSON serialization"""
        return {
            "title": self.title,
            "author": self.author,
            "isbn": self.isbn,
            "availability": self.availability
        }
    
    # Create Book from dictionary (useful for JSON loading)
    @classmethod
    def from_dict(cls, data):
        """Creates a Book object from dictionary data"""
        book = cls(data["title"], data["author"], data["isbn"])
        book.availability = data["availability"]
        return book