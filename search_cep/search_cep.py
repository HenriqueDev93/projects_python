""" Busca CEP
Objetivo: criar uma função com recursão à uma API que verifica o cep informado.
API: Application Programming Interface (Interface de Programação de Aplicação).
Passos:
1. Importar a biblioteca necessária para fazer a requisição à API;
2. criar a função com tratamento de erros.

API docs: https://docs.awesomeapi.com.br/ """

import requests as rq

def search_cep(input_cep):
    """ a função recebe um número ou string de um cep e envia para o site da API pela biblioteca """
    request_cep = rq.get(f'https://cep.awesomeapi.com.br/json/{input_cep}')
    requisition_cep = request_cep.json()
    """ os dados são retornados em json e precisam ser transformados em uma lista """
    try:
        user_cep = requisition_cep['cep']
        user_address = requisition_cep['address']
        user_district = requisition_cep['district']
        user_city_state = f'{requisition_cep["city"]}-{requisition_cep["state"]}'
        user_ddd = requisition_cep['ddd']

        """ é feito o tratamento de dados para o retorno em uma string
         obs: a string poderia ser feita sem o uso de variáveis, não foi feito por questões didáticas """
        map_address = f'{requisition_cep['lat']},{requisition_cep['lng']}'
        return f'CEP: {user_cep}', f'Endereço: {user_address}', f'Bairro: {user_district}', f'Cidade-Estado: {user_city_state}', f'DDD: {user_ddd} | {map_address}'
    except:
        return 'CEP inválido, tente novamente'

if __name__ == '__main__':
    print(search_cep('6516516516'))
    print(search_cep('38408000'))
    print(search_cep('04929-340'))
    print(search_cep('22220-001'))
