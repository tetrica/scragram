from user import User
from getpass import getpass

if __name__ == '__main__':
    user_data ={}

    user_data['username'] = input('Username: ')
    user_data['password'] = getpass()

    user = User(
        user_data['username'],
        user_data['password']
    )

    user.login()
    user.follow('arquivos_de_testes/745GeneralUsers.txt')
    user.like('arquivos_de_testes/city.txt')