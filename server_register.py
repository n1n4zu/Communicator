import socket
import threading
import sqlite3


IP = '0.0.0.0'
PORT = 9996


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
        received_datas = client_socket.recv(4096).decode()
        datas = received_datas.split('\n')
        conn = sqlite3.connect('users.db')
        cursor = conn.cursor()

        question = cursor.execute(f"SELECT name FROM user_data WHERE name LIKE '{datas[0]}'").fetchall()
        question = bool(question)

        if question:
            response = 'Już istnieje użytkownik o takiej nazwie'
        else:
            try:
                cursor.execute("INSERT INTO user_data (name, password) VALUES (?, ?)", (datas[0], datas[1]))
                conn.commit()
                response = 'Zarejestrowano użytkownika'
            except sqlite3.Error as e:
                print("Błąd podczas wstawiania danych:", e)
                response = 'Nie udało się zarejestrować użytkownika'
            finally:
                conn.close()

        sock.send(response.encode('utf-8'))


if __name__ == '__main__':
    main()

