# Step 3: Encapsulation and data hiding
from models.book import Book
from models.member import Member
from models.transaction import Transaction
from utils.file_handler import FileHandler
import json

class Library:
    """
    Library class manages all books, members, and transactions.
    Demonstrates encapsulation by hiding internal data structures.
    """
    
    def __init__(self, name="My Library"):
        """
        Initialize the library system.
        
        Parameters:
        - name: Name of the library
        """
        self.__name = name  # Private attribute (encapsulation)
        self.__books = []   # Private list of Book objects
        self.__members = [] # Private list of Member objects
        self.__transactions = []  # Private list of Transaction objects
        self.__file_handler = FileHandler()
        
        # Load existing data
        self.__load_data()
        
        print(f"\n{'='*50}")
        print(f"Welcome to {self.__name}!")
        print(f"{'='*50}\n")
    
    # Private methods (can't be accessed outside the class)
    def __load_data(self):
        """Load all data from JSON files"""
        # Load books
        books_data = self.__file_handler.read_json("data/books.json")
        self.__books = [Book.from_dict(data) for data in books_data]
        
        # Load members
        members_data = self.__file_handler.read_json("data/members.json")
        self.__members = [Member(data["name"], data["member_id"]) for data in members_data]
        
        # Reconstruct borrowed books for members
        for member_data, member in zip(members_data, self.__members):
            for isbn in member_data["borrowed_books"]:
                book = self.find_book_by_isbn(isbn)
                if book:
                    member.borrowed_books.append(book)
    
    def __save_data(self):
        """Save all data to JSON files"""
        # Save books
        books_data = [book.to_dict() for book in self.__books]
        self.__file_handler.write_json("data/books.json", books_data)
        
        # Save members
        members_data = [member.to_dict() for member in self.__members]
        self.__file_handler.write_json("data/members.json", members_data)
        
        # Save transactions
        transactions_data = [trans.to_dict() for trans in self.__transactions]
        self.__file_handler.write_json("data/transactions.json", transactions_data)
    
    # Public methods (API of the Library class)
    def add_book(self, title, author, isbn):
        """
        Add a new book to the library.
        
        Parameters:
        - title: Book title
        - author: Book author
        - isbn: ISBN number
        """
        # Validate ISBN
        if not Book.validate_isbn(isbn):
            print("Error: Invalid ISBN format. Must be 10 or 13 digits.")
            return None
        
        # Check if book already exists
        existing_book = self.find_book_by_isbn(isbn)
        if existing_book:
            print(f"Error: Book with ISBN {isbn} already exists.")
            return None
        
        # Create and add new book
        new_book = Book(title, author, isbn)
        self.__books.append(new_book)
        self.__save_data()
        print(f"Book added: {new_book}")
        return new_book
    
    def remove_book(self, isbn):
        """
        Remove a book from the library.
        
        Parameters:
        - isbn: ISBN of the book to remove
        """
        book = self.find_book_by_isbn(isbn)
        if book:
            if not book.availability:
                print(f"Cannot remove '{book.title}' - it's currently borrowed.")
                return False
            
            self.__books.remove(book)
            self.__save_data()
            print(f"Book removed: '{book.title}'")
            return True
        else:
            print(f"No book found with ISBN: {isbn}")
            return False
    
    def register_member(self, name, member_id=None):
        """
        Register a new library member.
        
        Parameters:
        - name: Member's name
        - member_id: Optional custom ID (auto-generated if not provided)
        """
        # Auto-generate member ID if not provided
        if member_id is None:
            member_id = f"M{len(self.__members) + 1:04d}"
        
        # Check if member ID already exists
        if self.find_member_by_id(member_id):
            print(f"Error: Member with ID {member_id} already exists.")
            return None
        
        # Create and add new member
        new_member = Member(name, member_id)
        self.__members.append(new_member)
        self.__save_data()
        return new_member
    
    def issue_book(self, isbn, member_id):
        """
        Issue a book to a member.
        
        Parameters:
        - isbn: ISBN of the book to issue
        - member_id: ID of the member borrowing the book
        """
        # Find book and member
        book = self.find_book_by_isbn(isbn)
        member = self.find_member_by_id(member_id)
        
        # Error handling
        if not book:
            print(f"Error: No book found with ISBN {isbn}")
            return False
        
        if not member:
            print(f"Error: No member found with ID {member_id}")
            return False
        
        if not book.availability:
            print(f"Error: '{book.title}' is already borrowed.")
            return False
        
        # Process the borrowing
        if member.borrow_book(book):
            book.toggle_availability()
            
            # Create transaction record
            transaction = Transaction(member, book, "issue")
            self.__transactions.append(transaction)
            
            self.__save_data()
            return True
        return False
    
    def return_book(self, isbn, member_id):
        """
        Process book return.
        
        Parameters:
        - isbn: ISBN of the book being returned
        - member_id: ID of the member returning the book
        """
        # Find book and member
        book = self.find_book_by_isbn(isbn)
        member = self.find_member_by_id(member_id)
        
        # Error handling
        if not book:
            print(f"Error: No book found with ISBN {isbn}")
            return False
        
        if not member:
            print(f"Error: No member found with ID {member_id}")
            return False
        
        if book.availability:
            print(f"Error: '{book.title}' is not currently borrowed.")
            return False
        
        # Process the return
        if member.return_book(book):
            book.toggle_availability()
            
            # Create transaction record
            transaction = Transaction(member, book, "return")
            self.__transactions.append(transaction)
            
            self.__save_data()
            return True
        return False
    
    def search_books(self, query):
        """
        Search for books by title, author, or ISBN.
        
        Parameters:
        - query: Search term
        """
        query = query.lower()
        results = []
        
        for book in self.__books:
            if (query in book.title.lower() or 
                query in book.author.lower() or 
                query in book.isbn):
                results.append(book)
        
        return results
    
    def find_book_by_isbn(self, isbn):
        """Find a book by its ISBN"""
        for book in self.__books:
            if book.isbn == isbn:
                return book
        return None
    
    def find_member_by_id(self, member_id):
        """Find a member by their ID"""
        for member in self.__members:
            if member.member_id == member_id:
                return member
        return None
    
    def get_all_books(self):
        """Returns list of all books"""
        return self.__books
    
    def get_all_members(self):
        """Returns list of all members"""
        return self.__members
    
    def get_available_books(self):
        """Returns list of available books"""
        return [book for book in self.__books if book.availability]
    
    def get_borrowed_books(self):
        """Returns list of borrowed books"""
        return [book for book in self.__books if not book.availability]
    
    def get_transaction_history(self):
        """Returns transaction history"""
        return self.__transactions
    
    def display_books(self):
        """Display all books in the library"""
        print("\n" + "="*50)
        print("ALL BOOKS")
        print("="*50)
        for i, book in enumerate(self.__books, 1):
            print(f"{i}. {book}")
    
    def display_members(self):
        """Display all members"""
        print("\n" + "="*50)
        print("ALL MEMBERS")
        print("="*50)
        for i, member in enumerate(self.__members, 1):
            print(f"{i}. {member}")
    
    def display_statistics(self):
        """Display library statistics"""
        print("\n" + "="*50)
        print("LIBRARY STATISTICS")
        print("="*50)
        print(f"Total Books: {len(self.__books)}")
        print(f"Available Books: {len(self.get_available_books())}")
        print(f"Borrowed Books: {len(self.get_borrowed_books())}")
        print(f"Total Members: {len(self.__members)}")
        print(f"Total Transactions: {len(self.__transactions)}")