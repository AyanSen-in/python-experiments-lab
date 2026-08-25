# Step 5: Working with files and JSON
import json
import os

class FileHandler:
    """
    Utility class for handling JSON file operations.
    """
    
    def __init__(self):
        """Initialize file handler and ensure directories exist"""
        self.ensure_directories()
    
    def ensure_directories(self):
        """Create necessary directories if they don't exist"""
        directories = ["data"]
        for directory in directories:
            if not os.path.exists(directory):
                os.makedirs(directory)
                print(f"Created directory: {directory}")
    
    def read_json(self, filepath):
        """
        Read data from a JSON file.
        Returns empty list if file doesn't exist.
        
        Parameters:
        - filepath: Path to the JSON file
        """
        try:
            with open(filepath, 'r') as file:
                return json.load(file)
        except FileNotFoundError:
            # Return empty list if file doesn't exist
            self.write_json(filepath, [])
            return []
        except json.JSONDecodeError:
            print(f"Error: Invalid JSON in {filepath}")
            return []
    
    def write_json(self, filepath, data):
        """
        Write data to a JSON file.
        
        Parameters:
        - filepath: Path to the JSON file
        - data: Data to write (must be JSON serializable)
        """
        try:
            with open(filepath, 'w') as file:
                json.dump(data, file, indent=2)
            return True
        except Exception as e:
            print(f"Error writing to {filepath}: {e}")
            return False