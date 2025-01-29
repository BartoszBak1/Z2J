import json
import os

class Database():
    def __init__(self) -> None:
        self.database_path = "/Projects/zero_to_junior/backend/python_201/data" 
        self.file_users = "users.json"
        self.file_messages = "messages.json"

    def save_data(self, path, file_name, data):
            with open(os.path.join(path, file_name), "w") as file:
                json.dump(data, file)

    def load_data(self, path, file_name):
        with open(os.path.join(path, file_name), "r") as file:
            return json.load(file)
        
    def check_if_user_exist(self, users, username):
        
        for user in users:
            if username == user["username"]:
                return True
        return False

    def check_credentials(self, user, username, password):
        try:
            if username == user["username"] and password == user["password"]:
                return True
            else:
                return False
        except TypeError:
            return False   

    def get_user_data(self, data, username):

        for user in data:
            if user['username'] == username:
                return user
            
        return None
    
    def get_user_msgs(self, data, username):
        
        msgs = []
        for msg in data:
            if msg['sender'] == username:
                msgs.append({'receiver': msg['receiver'], 'message': msg['message']})
            
        return msgs

    def update_unread_msgs(self, users, username, new_count):
        for user in users:
            if user['username'] == username:
               user['unread_msgs'] = new_count
               return True
        return False
