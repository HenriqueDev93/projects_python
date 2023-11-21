""" Conversor de Moedas
Objetivo: criar uma função com recursão à uma API que converte moedas (taxa de câmbio).
API: Application Programming Interface (Interface de Programação de Aplicação).
Passos:
1. Importar a biblioteca necessária para fazer a requisição à API;
2. criar e executar a função.

API docs: https://docs.awesomeapi.com.br/ """

import requests as rq

dolar = 'USD'
euro = 'EUR'
iene = 'JPY'
real = 'BRL'

def currency_converter(moeda1: str, moeda2: str, value_num: float) -> float:
    requisition = rq.get(
        f'https://economia.awesomeapi.com.br/last/{moeda1}-{moeda2}')
    requisition_dic = requisition.json()
    return float(requisition_dic[f'{moeda1}{moeda2}']['bid']) * value_num

if __name__ == '__main__':
    print(f'{currency_converter(real, dolar, 50000):,.2f}')
    print(f'{currency_converter(dolar, real, 50000):,.2f}')
    print(f'{currency_converter(dolar, real, 10275):,.2f}')
