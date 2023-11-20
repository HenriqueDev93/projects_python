""" Gerador de senhas
Objetivo: criar um gerador de senhas de acordo com o que for solicitado
    (quantidade de caracteres, se são números, letras maiúsculas, letras minúsculas e/ou caracteres especiais).
Passos:
1. importar as bibliotecas necessárias para a criação do código;
2. criar a função que traz randômicamente caracteres para a senha. """

from string import ascii_lowercase, ascii_uppercase, digits, punctuation # letras minúsculas, maiúscuras, números e caracteres especiais
import random

def password_generator(how_many: int, pass_types: list) -> str:
    new_pass: str = ''
    """ a variável nova senha permanece vazia até que caracteres sejam adicionados, um a um """
    while len(new_pass) < how_many:
        random_list = random.choice(pass_types)
        new_pass += random.choice(random_list)
    return new_pass
""" uma senha é retornada após o final do processo """

if __name__ == '__main__':
    try:
        how_many: int = int(input('Quantos caracteres sua senha precisa ter? '))
        print(password_generator(how_many, [ascii_lowercase, ascii_uppercase, digits, punctuation]))
    except:
        print('Apenas números são permitidos.')
