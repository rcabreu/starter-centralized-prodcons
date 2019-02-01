import socket
import pickle
from models import message

HOST = '127.0.0.1'
PORT = 12345

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    message = message.Message()
    message.command = 'PUT'
    message.value = 9
    bytes = pickle.dumps(message)
    print (len(bytes))
    s.send(bytes)