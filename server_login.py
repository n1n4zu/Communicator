import socket
import threading
import sqlite3


IP = '0.0.0.0'
PORT = 9997


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


def handle_client(client_socket):
    with client_socket as sock:
        request = sock.recv(1024).decode('utf-8')
        conn = sqlite3.connect('users.db')
        cursor = conn.cursor()
        question = cursor.execute("SELECT name, password FROM user_data WHERE name LIKE ? OR password LIKE ?", (request, request)).fetchall()
        question = bool(question)

        if question:
            sock.send('1'.encode('utf-8'))
        else:
            sock.send('0'.encode('utf-8'))

        conn.close()


if __name__ == '__main__':
    main()

