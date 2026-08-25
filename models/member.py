# Step 2: Working with lists and more complex objects
from datetime import datetime

class Member:
    """
    Member class represents a library member.
    This class demonstrates composition (has-a relationship with Book).
    """
    
    # Class variable
    total_members = 0
    
    def __init__(self, name, member_id):
        """
        Initialize a new library member.
        
        Parameters:
        - name: Member's full name
        - member_id: Unique identifier for the member
        """
        self.name = name
        self.member_id = member_id
        self.borrowed_books = []  # List of Book objects
        self.membership_date = datetime.now().strftime("%Y-%m-%d")
        
        # Increment member count
        Member.total_members += 1
        
        print(f"Member registered: {self.name} (ID: {self.member_id})")
    
    # Instance method to borrow a book
    def borrow_book(self, book):
        """
        Add a book to the member's borrowed books list.
        
        Parameters:
        - book: Book object to borrow
        """
        if len(self.borrowed_books) < 5:  # Maximum 5 books per member
            self.borrowed_books.append(book)
            print(f"{self.name} borrowed '{book.title}'")
            return True
        else:
            print(f"{self.name} has reached the maximum limit of 5 books")
            return False
    
    # Instance method to return a book
    def return_book(self, book):
        """
        Remove a book from the member's borrowed books list.
        
        Parameters:
        - book: Book object to return
        """
        for borrowed in self.borrowed_books:
            if borrowed.isbn == book.isbn:
                self.borrowed_books.remove(borrowed)
                print(f"{self.name} returned '{book.title}'")
                return True
        
        print(f"{self.name} doesn't have '{book.title}'")
        return False
    
    # Get list of borrowed books
    def get_borrowed_books(self):
        """Returns list of currently borrowed books"""
        return self.borrowed_books
    
    # Get member information
    def get_info(self):
        """Returns formatted information about the member"""
        return f"Member: {self.name} (ID: {self.member_id}) - Books borrowed: {len(self.borrowed_books)}"
    
    # String representation
    def __str__(self):
        return self.get_info()
    
    # Convert to dictionary for JSON
    def to_dict(self):
        """Converts Member object to dictionary for JSON serialization"""
        return {
            "name": self.name,
            "member_id": self.member_id,
            "borrowed_books": [book.isbn for book in self.borrowed_books],
            "membership_date": self.membership_date
        }