import socket
import json 
from user import User
from message import Message
from datetime import datetime
from database import Database

class Server:
    def __init__(self, host, port, version) -> None:
        self.host = host
        self.port = port
        self.version = version
        self.start_time = datetime.now()
        self.logged_in_user = None
        self.logged_in_role = None
        self.options = {
            "uptime": self.uptime,
            "info": self.info,
            "help": self.help,
            "stop": self.stop,
            "signup": self.create_account,
            "login": self.login,
            "logout": self.logout,
            "send": self.send_msg_to_recipient,
            "read": self.read_msg}
        self.commands = {
            "uptime": "Returns the server's lifetime.",
            "info": "Returns the server's version number and date of creation.",
            "help": "Returns a list of available commands.",
            "stop": "Stop the server and the client simultaneously.",
            "signup": "Create a new account",
            "login": "Log in.",
            "logout": "Log out.",
            "send": "Send message.",
            "read": "Read message."
               }
        self.db = Database()
        
    def send_msg(self, conn, msg, code ='utf-8'):
        conn.sendall(msg.encode(code))

    def receive_msg(self, conn, code='utf-8'):
        return conn.recv(1024).decode(code)

    def start_server(self):

        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.bind((self.host, self.port))
            s.listen()
            conn, addr = s.accept()

            with conn:
                print(f"Connected by {addr}")

                while True:
                    data = self.receive_msg(conn)

                    if not data:
                        break

                    request = json.loads(data)
                    command = request.get('command')

                    try:
                        answer = self.options[command](**request)
                        self.send_msg(conn, msg = json.dumps(answer))
                    except KeyError:
                        self.send_msg(conn, msg = json.dumps('Wrong command')) 
                                

    def uptime(self, *args, **kwargs):

        return {"uptime": str(datetime.now() - self.start_time)}
    
    def info(self, *args, **kwargs):

        return {"version": self.version, 
                "stat_time": self.start_time.isoformat()}
    
    def stop(self, *args, **kwargs):
        
        return 'stop'

    def help(self, *args, **kwargs):
        
        return self.commands

    def create_account(self, **kwargs):
        
        username = kwargs.get('username')
        password = kwargs.get('password')
        role = kwargs.get('role')

        if role not in ['user', 'admin']:
            return {"status": "failure", 'message': 'Wrong role. Select user or admin.'}
        
        data = self.db.load_data(self.db.database_path, self.db.file_users)

        if self.db.check_if_user_exist(data, username):
            return {"status": "failure", "message": f"User with that name already exist."}
        else:
            user = User(username, password, role)
            data.append(user.__dict__)
            self.db.save_data(self.db.database_path, self.db.file_users, data)
            return {"status": "success", "message": f"You have created new account named {username}."}

            
    def login(self, **kwargs):

        username = kwargs.get('username')
        password = kwargs.get('password')
        data = self.db.load_data(self.db.database_path, self.db.file_users)
        
        if self.logged_in_user is not None:
            return {"status": "failure", "message": f"You are logged in as {self.logged_in_user}."}

        user = self.db.get_user_data(data, username)
        
        if  self.db.check_credentials(user, username, password):
            self.logged_in_user = username
            self.logged_in_role = user['role']
            return {"status": "success", "message": f"User {username} logged in."}
        else:
            return {"status": "failure", "message": f"Invalid username or password."}

    def logout(self, **kwargs):

        if self.logged_in_user: 
            username = self.logged_in_user
            self.logged_in_user = None
            self.logged_in_role = None
            return {"status": "success","message": f"User {username} logged out."}
        else:
            return {"status": "failure", "message": "No user is currently logged in"}


    def send_msg_to_recipient(self, **kwargs):

        recipient = kwargs['recipient']
        msg_content = kwargs['msg_content']

        if not self.logged_in_user:
            return {"status": "failure", "message": "No user is currently logged in."}
        if len(msg_content) > 255:
            return {"status": "failure", "message": "Message is to long."}
        
        users = self.db.load_data(self.db.database_path, self.db.file_users)
        user = self.db.get_user_data(users, recipient)
        if user is None:
            return {"status": "failure", "message": f"There is no such user like {recipient}."}
        
        unread_msgs = user['unread_msgs']
        if unread_msgs >= 5:
                    return {"status": "failure", "message": "Inbox is full."}        

        # save message
        message = Message(self.logged_in_user, recipient, msg_content)    
        messages = self.db.load_data(self.db.database_path, self.db.file_messages)
        messages.append(message.__dict__)
        self.db.save_data(self.db.database_path, self.db.file_messages, messages) 

        # update inbox
        unread_msgs = unread_msgs + 1
        self.db.update_unread_msgs(users, recipient, unread_msgs)
        self.db.save_data(self.db.database_path, self.db.file_users, users) 

        return {"status": "success", "message": f"The message has been sent to {recipient}."}

    def logout(self, **kwargs):

        username = self.logged_in_user
        self.logged_in_user = None

        return {"status": "success", "message": f"{username} logged out."}
    
    def read_msg(self, **kwargs):

        if not self.logged_in_user:
            return {"status": "failure", "message": "No user is currently logged in."}
        
        messages = self.db.load_data(self.db.database_path, self.db.file_messages)
        user_msgs = self.db.get_user_msgs_from_inbox( messages, self.logged_in_user)
        
        if len(user_msgs) == 0 and self.logged_in_role == 'user':
            return {"message": f"You don't have any messages."}
        else:
            # update user data
            users = self.db.load_data(self.db.database_path, self.db.file_users)
            self.db.update_unread_msgs(users, self.logged_in_user, 0)
            self.db.save_data(self.db.database_path, self.db.file_users, users)

            if self.logged_in_role == 'admin':
                return messages
            else:
                return user_msgs