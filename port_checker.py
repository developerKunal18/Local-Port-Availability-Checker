import socket

port = int(input("Enter port number: "))

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

result = sock.connect_ex(("localhost", port))

if result == 0:
    print(f"Port {port} is already in use")
else:
    print(f"Port {port} is available")

sock.close()
