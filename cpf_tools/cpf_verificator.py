""" Verificador de CPF
Objetivo: criar um verificador de CPF com tratamento de números iguais e letras.
Passos:
1. importar as bibliotecas necessárias para a criação do código;
2. criar uma lista de cpf já verificados;
3. criar a função que retorna 'True' ou 'False' com tratamento de erros.

Source: https://www.macoratti.net/alg_cpf.htm """

import re # utilizada para localizar strings
from string import punctuation # utilizada para limpeza do valor informado

cpf_list = ['111.444.777-35', '30579519023', '14643350016', '007.044.800-00',
            '546.546.565-58', '894.575.198-84', '132.788.469-12', '786.615.942-00', 'oek.dju.fjh.pq', '111.111.111-11']  # 4 true, 6 false, 1 only letters, 1 same number


def cpf_verificator(user_cpf: str) -> bool: # only strings are accepted, no treatment to integers
    try:
        user_cpf = str(user_cpf)
        clean_cpf = re.sub(f'[A-zÀ-ú_{punctuation}]', '', user_cpf)
        """ clean_cpf executa a limpeza dos dados informados à função """
        if len(set(clean_cpf)) == 1: return False
        """ len(set()) verifica se o cpf possui apenas um número repetido 11 vezes """
        new_cpf = clean_cpf[:9]
        """ new_cpf inicia a verificação do cpf (verificar as regras em source) """
        first_digit = for_in(10, clean_cpf)
        new_cpf = new_cpf + str(first_digit)
        second_digit = for_in(11, new_cpf)
        new_cpf = new_cpf + str(second_digit)
        """ cpf verdadeiro criado de acordo com os 9 primeiros números do cpf informado  """
        return new_cpf == clean_cpf
    except:
        return False


def for_in(range_num: int, cpf_num: str) -> int:
    """ função que executa os cálculos para a criação do novo cpf, em conforme com as regras """
    digit, first_sum = 0, 0
    for i in range(range_num, 1, -1):
        first_sum += i * int(cpf_num[digit])
        digit += 1
    first_rest = first_sum % 11
    if first_rest < 2: return 0
    return 11 - first_rest


if __name__ == '__main__': # permite a importação para outro arquivo python
    for cpf in cpf_list: print(cpf_verificator(cpf))
