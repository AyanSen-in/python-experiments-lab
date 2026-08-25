# Step 6: Putting it all together
from models.library import Library
import sys

class LibraryApp:
    """
    Main application class that provides the user interface.
    """
    
    def __init__(self):
        """Initialize the application"""
        self.library = Library("Community Library")
    
    def display_menu(self):
        """Display the main menu"""
        print("\n" + "="*50)
        print("LIBRARY MANAGEMENT SYSTEM")
        print("="*50)
        print("1. Add Book")
        print("2. Remove Book")
        print("3. Register Member")
        print("4. Issue Book")
        print("5. Return Book")
        print("6. Search Books")
        print("7. Display All Books")
        print("8. Display All Members")
        print("9. Display Statistics")
        print("10. View Transaction History")
        print("0. Exit"  )
        print("~"*50)
    
    def get_input(self, prompt):
        """Get user input with prompt"""
        return input(prompt).strip()
    
    def add_book_flow(self):
        """Flow for adding a book"""
        print("\n--- Add New Book ---")
        title = self.get_input("Enter book title: ")
        author = self.get_input("Enter book author: ")
        isbn = self.get_input("Enter ISBN (10 or 13 digits): ")
        
        if title and author and isbn:
            self.library.add_book(title, author, isbn)
        else:
            print("Error: All fields are required")
    
    def remove_book_flow(self):
        """Flow for removing a book"""
        print("\n--- Remove Book ---")
        isbn = self.get_input("Enter ISBN of book to remove: ")
        
        if isbn:
            self.library.remove_book(isbn)
        else:
            print("Error: ISBN is required")
    
    def register_member_flow(self):
        """Flow for registering a member"""
        print("\n--- Register New Member ---")
        name = self.get_input("Enter member name: ")
        custom_id = self.get_input("Enter custom ID (optional, press Enter for auto): ")
        
        if name:
            if custom_id:
                self.library.register_member(name, custom_id)
            else:
                self.library.register_member(name)
        else:
            print("Error: Name is required")
    
    def issue_book_flow(self):
        """Flow for issuing a book"""
        print("\n--- Issue Book ---")
        isbn = self.get_input("Enter book ISBN: ")
        member_id = self.get_input("Enter member ID: ")
        
        if isbn and member_id:
            self.library.issue_book(isbn, member_id)
        else:
            print("Error: Both ISBN and Member ID are required")
    
    def return_book_flow(self):
        """Flow for returning a book"""
        print("\n--- Return Book ---")
        isbn = self.get_input("Enter book ISBN: ")
        member_id = self.get_input("Enter member ID: ")
        
        if isbn and member_id:
            self.library.return_book(isbn, member_id)
        else:
            print("Error: Both ISBN and Member ID are required")
    
    def search_books_flow(self):
        """Flow for searching books"""
        print("\n--- Search Books ---")
        query = self.get_input("Enter search term (title, author, or ISBN): ")
        
        if query:
            results = self.library.search_books(query)
            if results:
                print(f"\nFound {len(results)} book(s):")
                for i, book in enumerate(results, 1):
                    print(f"{i}. {book}")
            else:
                print("No books found matching your search.")
        else:
            print("Error: Search term is required")
    
    def view_transactions_flow(self):
        """Flow for viewing transaction history"""
        transactions = self.library.get_transaction_history()
        
        if transactions:
            print("\n--- Transaction History ---")
            for i, transaction in enumerate(transactions[-20:], 1):  # Show last 20
                print(f"{i}. {transaction}")
        else:
            print("No transactions recorded yet.")
    
    def run(self):
        """Main application loop"""
        while True:
            self.display_menu()
            
            try:
                choice = int(self.get_input("Enter your choice (0-10): "))
            except ValueError:
                print("Error: Please enter a valid number")
                continue
            
            if choice == 0:
                print("\nThank you for using the Library Management System!")
                print("Goodbye!")
                sys.exit(0)
            elif choice == 1:
                self.add_book_flow()
            elif choice == 2:
                self.remove_book_flow()
            elif choice == 3:
                self.register_member_flow()
            elif choice == 4:
                self.issue_book_flow()
            elif choice == 5:
                self.return_book_flow()
            elif choice == 6:
                self.search_books_flow()
            elif choice == 7:
                self.library.display_books()
            elif choice == 8:
                self.library.display_members()
            elif choice == 9:
                self.library.display_statistics()
            elif choice == 10:
                self.view_transactions_flow()
            else:
                print("Error: Please enter a number between 0 and 10")

# Entry point of the program
if __name__ == "__main__":
    app = LibraryApp()
    app.run()