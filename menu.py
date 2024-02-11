from clear import Clear
import sys


def Menu():
    Clear()

    while True:
        print('''[1] Zaloguj
[2] Zarejestruj się
[3] Wyjdź''')
        option = input('\n>')

        match option.lower():
            case '1':
                return 'login'
            case 'zaloguj':
                return 'login'
            case '2':
                return 'register'
            case 'zarejestruj.*':
                return 'register'
            case '3':
                sys.exit()
            case 'wyjdź':
                sys.exit()
            case _:
                pass
