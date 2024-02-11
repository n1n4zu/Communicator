import socket
from clear import Clear
from login import Login
from register import Register
from menu import Menu

while True:
    option = Menu()

    if option == 'register':
        Register()
        input()

    elif option == 'login':
        if Login():
            from login import login

            Clear()

            while True:
                client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

                client.connect(("192.168.0.137", 9998))

                message = input(f'{login}> ')

                if message == 'exit':
                    client.close()
                    break

                else:
                    message = f'{login}> {message}'

                    bajty = message.encode("utf-8")

                    client.send(bajty)

                    response = client.recv(4096)

                    Clear()

                    print(response.decode())
