from getpass import getpass
from hash import Hash
import socket
from clear import Clear


def Register():
    Clear()
    print('Proszę się zarejestrować')

    login = input('Login: ')
    password = getpass('Hasło: ')

    if login == '' or password == '':
        print('Dane logowania nie mogą być puste!')
    else:
        password = Hash(password)

        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.connect(("192.168.0.137", 9996))
        datas = [login, password]
        message = '\n'.join(datas).encode('utf-8')
        client.send(message)
        response = client.recv(4096).decode('utf-8')
        print(response)
        client.close()
