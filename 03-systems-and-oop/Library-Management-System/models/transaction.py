# Step 4: Creating complex classes with multiple attributes
from datetime import datetime

class Transaction:
    """
    Transaction class to track book borrowing history.
    """
    
    def __init__(self, member, book, transaction_type):
        """
        Initialize a new transaction.
        
        Parameters:
        - member: Member object
        - book: Book object
        - transaction_type: "issue" or "return"
        """
        self.member = member
        self.book = book
        self.transaction_type = transaction_type
        self.timestamp = datetime.now()
    
    def get_info(self):
        """Returns formatted transaction information"""
        return f"{self.timestamp}: {self.member.name} {self.transaction_type}d '{self.book.title}'"
    
    def __str__(self):
        return self.get_info()
    
    def to_dict(self):
        """Convert transaction to dictionary for JSON"""
        return {
            "member_id": self.member.member_id,
            "book_isbn": self.book.isbn,
            "transaction_type": self.transaction_type,
            "timestamp": self.timestamp.strftime("%Y-%m-%d %H:%M:%S")
        }