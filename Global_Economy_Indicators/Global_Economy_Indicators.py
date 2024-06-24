# importando a biblioteca e o módulo:

import pandas as pd
import plotly.express as px

sheet = pd.read_csv('C:/Users/henri/Documents/Estudos/Programação/Python/projetos/projs_p_site/Global_Economy_Indicators/Global_Economy_Indicators.csv')

# tratando os dados

for column in sheet.columns:
    sheet.rename(columns={column: ''.join(column.split())}, inplace=True)

for line in sheet['Country']:
    sheet['Country'].replace({line: ''.join(line.split())}, inplace=True)

sheet = sheet.set_index('CountryID')

# gráfico população mundial
fig_pop_yr = px.bar(sheet, x='Year', y='Population', title='População mundial')

afghanistan = sheet[sheet['Country'] == 'Afghanistan']

afghanistan_fig_pop_yr = px.bar(
    afghanistan, x='Year', y='Population', title='Afghanistan', template="gridon")  # gráfico Afeganistão

south_america = ['Argentina', 'Bolivia(PlurinationalStateof)', 'Brazil', 'Chile', 'Colombia',
                 'Ecuador', 'Guyana', 'Paraguay', 'Peru', 'Suriname', 'Uruguay', 'Venezuela(BolivarianRepublicof)']

# função padrão para criar o gráfico população x ano de qualquer país ou lista de países


def create_fig_pop_yr(country):  # a função recebe o nome de um país
    # variável que filtra o país especificado
    name_country = sheet[sheet['Country'] == country]
    # variável que cria a figura do gráfico
    country_fig = px.bar(name_country, x='Year', y='Population', title=country, template="seaborn")
    country_fig.show()  # comando que exibe o gráfico

# função para criar gráficos de acordo com os parâmetros, default: população x ano do Brasil


def create_fig(axis_x='Year', axis_y='Population', country='Brazil'):
    name_country = sheet[sheet['Country'] == country]
    fig = px.bar(name_country, x=axis_x, y=axis_y, title=country, template='plotly_dark')
    fig.show()


if __name__ == '__main__':
    sheet.info()

    print(sheet)

    afghanistan_fig_pop_yr.show()  # gráfico Afeganistão

    for country in south_america:  # "for loop" que envia um país por vez para a função de criação de gráficos
        create_fig_pop_yr(country)

    create_fig()  # função sendo chamada com os valores 'default'

    # função sendo chamada com valores especificados
    create_fig('Year', 'GrossDomesticProduct(GDP)', 'UnitedStates')

    # função sendo chamada com valores especificados
    create_fig('Year', 'PercapitaGNI', 'UnitedStates')
