import socket
import threading


def get_ip_address():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    return s.getsockname()[0]


def receive_messages( clientIP ):


    while True:
        data = clientsocket.recv(1024)

        msg = data.decode()
        print(f"{clientIP}: {msg}")

    

serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = get_ip_address()
port = 8000

serversocket.bind((host, port))

serversocket.listen(5)

print("Server started and listening...")




while True:
    (clientsocket, address) = serversocket.accept()
    clientIP = address[0]
    print (f"Connection found from {clientIP}!")

    x = threading.Thread(target=receive_messages, args=( clientIP, ) )
    x.start()

    
    
    
