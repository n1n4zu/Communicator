import socket
import threading
import re


IP = '0.0.0.0'
PORT = 9998


def main():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((IP, PORT))
    server.listen(5)
    print(f'[*] Nasłuchiwanie na {IP}:{PORT}')

    while True:
        client, address = server.accept()
        print(f'[*] Przyjęto połączenie od {address[0]}:{address[1]}')
        client_handler = threading.Thread(target=handle_client, args=(client,))
        client_handler.start()


def save_to_file(message, file='history.txt'):
    with open(file, 'a') as plik:
        plik.write(f'{message}\n')


def read_file(file='history.txt'):
    with open(file, 'r') as plik:
        return plik.read()


def handle_client(client_socket):
    with client_socket as sock:
        request = sock.recv(1024)
        decoded_request = request.decode('utf-8').strip()
        if re.match(r'^[^>]+> $', decoded_request):
            response = read_file().encode('utf-8')
            sock.send(response)
        elif re.match(r'^[^>]+> .+', decoded_request):
            print(f'[*] Odebrano: {decoded_request}')
            save_to_file(decoded_request)
            response = read_file().encode('utf-8')
            sock.send(response)
        else:
            response = read_file().encode('utf-8')
            sock.send(response)


if __name__ == '__main__':
    main()
