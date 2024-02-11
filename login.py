from getpass import getpass
from hash import Hash
import socket
from clear import Clear

login = None


def Login():
    global login
    attempts = 3

    while attempts > 0:
        Clear()
        print('Proszę się zalogować')

        login = input('Login: ')
        password = getpass('Hasło: ')
        password = Hash(password).encode('utf-8')

        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.connect(("192.168.0.137", 9997))
        client.send(login.encode('utf-8'))
        response1 = client.recv(4096)
        client.close()

        if response1.decode('utf-8') == '1':
            client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            client.connect(("192.168.0.137", 9997))
            client.send(password)
            response2 = client.recv(4096)
            client.close()
            if response2.decode('utf-8') == '1':
                login = login
                return True
            else:
                attempts -= 1
        else:
            attempts -= 1

    return False
