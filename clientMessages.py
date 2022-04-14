
import socket


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = '10.255.8.207'
port = 8000
s.connect( (host, port) )



print("Cilent started...")

while True:

    msg = input("Send: ")
    if msg == "":
        break

    s.send( msg.encode() )
    



s.close()
