import socket
import json 
from datetime import datetime


HOST = "127.0.0.1"  # The server's hostname or IP address
PORT = 65432  # The port used by the server
VERSION = '0.0.1'

class Server:
    def __init__(self, host, port, version) -> None:
        self.host = host
        self.port = port
        self.version = version
        self.start_time = datetime.now()

    def start_server(self):

        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.bind((self.host, self.port))
            s.listen()
            conn, addr = s.accept()

            with conn:
                print(f"Connected by {addr}")

                while True:
                    data = conn.recv(1024).decode("utf-8")
                    if not data:
                        break
                    if data == 'help':
                        conn.sendall(json.dumps(self.commands()).encode('utf-8'))
                    elif data == 'info':
                        conn.sendall(self.info().encode('utf-8'))
                    elif data == 'uptime':
                        conn.sendall(self.uptime().encode('utf-8'))
                    elif data == 'stop':
                        conn.sendall(data.encode('utf-8'))
                        s.close()
                        break
                    else:
                        conn.sendall(('Unknown command').encode('utf-8'))

    def uptime(self):
        return json.dumps({"uptime": str(datetime.now() - self.start_time)})
    
    def info(self):
        return json.dumps({"version": self.version, 
                           "stat_time": self.start_time.isoformat()})
    
    def commands(self):

        msg = {
            "uptime": "Returns the server's lifetime.",
            "info": "Returns the server's version number and date of creation.",
            "help": "Returns a list of available commands.",
            "stop": "Stop the server and the client simultaneously."
               }
        
        return msg

if __name__ == '__main__':
    server = Server(HOST, PORT, VERSION)
    server.start_server()