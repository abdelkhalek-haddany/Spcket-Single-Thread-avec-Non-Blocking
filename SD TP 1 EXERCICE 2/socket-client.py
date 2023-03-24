import socket
import threading

HOST = 'localhost'
PORT = 4444

def handle_response(sock):
    while True:
        response = sock.recv(1024)
        if not response:
            break
        print(response.decode())

def main():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.connect((HOST, PORT))
        threading.Thread(target=handle_response, args=(sock,), daemon=True).start()
        while True:
            request = input()
            sock.sendall(request.encode() + b'\n')

if __name__ == '__main__':
    main()
