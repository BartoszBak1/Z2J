import socket
import json

class Client:
    def __init__(self) -> None:
        self.host = "127.0.0.1"
        self.port = 65432 

    def start_connection(self):
        print("Connected to the server.")
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((self.host, self.port))

            while True:
                msg = input("\nEnter the command. Type 'help' to print command list: ").strip() 
                s.sendall(msg.encode('utf-8'))
                data = s.recv(1024).decode('utf-8')

                if data == 'stop':
                    print("The server has been closed.")
                    break
                else:
                    try:
                        response = json.loads(data)
                        if isinstance(response, dict):
                            print()
                            for key, value in response.items():
                                print(f'{key}: {value}')
                        else:
                            print(f'\n{response}')
                    except json.JSONDecodeError:
                        print(f'\n{data}')

                
if __name__ == '__main__':
    client = Client()
    client.start_connection()

