""" Gerador de CPF
Objetivo: criar um gerador de CPF usando o cpf_verificator para confirmar se o cpf é valido.
Passos:
1. importar a biblioteca necessária para a criação do código;
2. importar o código verificador de cpf;
3. criar um novo cpf randômico; """

import random # biblioteca que informa números aleatórios em uma faixa estabelecida
from cpf_verificator import cpf_verificator


def cpf_generator():
    while True: # a função executa até um cpf verdadeiro ser criado
        new_cpf = ''
        for _ in range(0, 11):
            new_cpf += str(random.randint(0, 9))
        cpf_verifier = cpf_verificator(new_cpf) # cpf criado é verificado em cpf_verificator
        if cpf_verifier: # se verdadeiro, o novo cpf é retornado
            return f'{new_cpf[:3]}.{new_cpf[3:6]}.{new_cpf[6:9]}-{new_cpf[9:]}'


if __name__ == "__main__":
    print(cpf_generator())

""" Possível melhoria: a função for_in poderia ser utilizada para informar os dois últimos números, assim, quase que quaisquer 9 números que o cpf_generator criasse, tornariam-se verdadeiros utilizando a função for_in, economizando memória. Mas este não era o objetivo. """