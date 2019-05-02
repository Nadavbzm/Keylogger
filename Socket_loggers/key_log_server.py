import socket

HOST = '127.0.0.1'  # Symbolic name, meaning all available interfaces
PORT = 53  # Arbitrary non-privileged port

#creating socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind socket to local host and port
s.bind((HOST, PORT))
print('Socket bind complete')

#listening on port
s.listen(10)

while True:
    #aceepting communication
    conn, addr = s.accept()
    print('Connected with ' + addr[0] + ':' + str(addr[1]))
    msg = conn.recv(1024).decode()
    print(msg)
    a = open("server_log.txt", "a")
    a.write(msg)
    a.close()


s.close()
