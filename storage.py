import json

class FileManager:
    def __init__(self, filename): #Constructor
        self.filename = filename

    #function to load data from the the json file
    def load_data(self):

        # Returns list: The loaded data as a list (if successful), otherwise an empty list.
        try:
            with open(self.filename, 'r') as file:
                return json.load(file)
        except FileNotFoundError:
            print(f"File {self.filename} not found. Creating new file.")
            return []
        except Exception as e:
            print(f"Error loading data from {self.filename}: {e}")
            return []

    def save_data(self, data):
        '''
        Saves the provided data to the specified file in JSON format.

        Args:
            data (list): The data to be saved.
        '''
        try:
            with open(self.filename, 'w') as file:
                json.dump(data, file, indent=4)
            print(f"Data saved to {self.filename}")
        except Exception as e:
            print(f"Error saving data to {self.filename}: {e}")

class BookFileManager(FileManager):
    #This class inherits from FileManager to handle specifically Book data in JSON files.
    def __init__(self, filename):
        '''
        Args:
         filename (str): The name of the file to be used for storing books data.
        '''
        super().__init__(filename) #super().__init__(filename) Used to call the Parent class Constructor

class UserFileManager(FileManager):
    #This class inherits from FileManager to handle specifically User data in JSON files.
    def __init__(self, filename):
        '''
        Args:
         filename (str): The name of the file to be used for storing user data.
        '''
        super().__init__(filename) #super().__init__(filename) Used to call the Parent class Constructor

class CheckoutManager(FileManager):
    #This class inherits from FileManager to handle specifically Checkout data in JSON files.
    def __init__(self,filename):
        '''
        Args:
         filename (str): The name of the file to be used for storing checkout data.
        '''
        super().__init__(filename) #super().__init__(filename) Used to call the Parent class Constructor

