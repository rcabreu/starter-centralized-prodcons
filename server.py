import socket
import pickle
from models import message


HOST = '0.0.0.0'
PORT = 12345

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen(0)
    conn, addr = s.accept()
    with conn:
        print('New ip has joined: ', addr)
        while True:
            data = b''
            l = 77
            while l > 0:
                d = conn.recv(l)
                l -= len(d)
                data += d
            message = pickle.loads(data)
            print(message.command + ' ' + str(message.value))
            
