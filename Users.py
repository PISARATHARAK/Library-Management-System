import logging
from models import User
from storage import UserFileManager


class Users:
    def __init__(self): #Constructor
        self.user_manager=UserFileManager("users.json")
        self.users=self.user_manager.load_data()

        # # Configure logging
        # logging.basicConfig(filename='user_operations.log', level=logging.INFO,
        #                     format='%(asctime)s - %(levelname)s - %(filepath) - %(message)s - File: %(pathname)s')
    #function to add users into users
    def add_user(self,name,user_id):
        new_user=User(name,user_id) #creating Object of user
        self.users.append(new_user.to_dict()) #Convert User object to dictionary for saving in json file
        self.user_manager.save_data(self.users) # Save updated data to json file

        logging.info(f"Added user: Name='{name}', User ID='{user_id}'")
    #function to update user 
    def update_user(self,user_id,new_name=None):
        for user in self.users:
            if user['user_id']==user_id:
                if new_name is not None:
                    user['name']=new_name #Updating Name 
                print(f"User with User ID {user_id} is Updated")
                self.user_manager.save_data(self.users) #Saving Updated data to json
                # Log the operation
                logging.info(f"Updated user with User ID '{user_id}': New name='{new_name}'")
                return True

        print(f"User with User id {user_id} not found")
        return False

    #function to delete user using various attributes
    def delete_user(self,user_id):
        for user in self.users:
            if user["user_id"]==user_id:
                self.users.remove(user) #deleting user from the Users list
                print(f"User with User Id {user_id} is Deleted")
                self.user_manager.save_data(self.users) #Saving back Users list to json
                # Log the operation
                logging.info(f"Deleted user with User ID '{user_id}'")
                return True
        print(f"User with User id {user_id} not found")
        return False

    #function to list all the users
    def list_users(self):
        if(len(self.users)==0):
            print("No users in the list")
            return 
        for user in self.users:
            print(user)
    
    #function to search for the user in users
    def search_user(self):
        while True:
            attribute = input("Enter the Attribute you want to search for:").lower()
            Valid = ["user_id", "name"]
            if attribute not in Valid:
                continue
            value = input(f"Enter the {attribute} you are searching for:")
            for user in self.users:
                if user[attribute] == value:
                    print(f"User with {attribute} {value} is found")
                    return True
            
            print(f"No User with {attribute} {value} is found")
            return False



if __name__ == "__main__":
    U1=Users()

    U1.add_user("Tharak",'1')
    U1.add_user("Sandeep",'2')
    U1.add_user("Rajesh",'3')
    U1.add_user("Sai",'4')
    U1.add_user("Sanjay",'5')
    U1.list_users()

    U1.update_user('3',new_name="Kanna")
    U1.update_user('1',new_name="Chanti")
    U1.list_users()

    U1.delete_user('2')
    U1.list_users()

    U1.search_user()