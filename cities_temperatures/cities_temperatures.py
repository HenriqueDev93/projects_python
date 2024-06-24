import os
import pandas as pd
import re
import plotly.graph_objects as go

[cities_mg, cities_rj, cities_sp, cities_go, cities_df, cities_ba] = [
    dict(), dict(), dict(), dict(), dict(), dict()]
for yr in range(2003, 2024):
    yr_list = os.listdir(f'cities_temperatures/assets/{yr}/')
    i = 0
    j = 0
    for _ in range(0, len(yr_list)):
        if yr_list[i][:11] == 'INMET_SE_MG':
            cities_mg[f'{yr}_{j}'] = (yr_list[i][17:-28])
            j += 1
        if yr_list[i][:11] == 'INMET_SE_SP':
            cities_sp[f'{yr}_{j}'] = (yr_list[i][17:-28])
            j += 1
        if yr_list[i][:11] == 'INMET_SE_RJ':
            cities_rj[f'{yr}_{j}'] = (yr_list[i][17:-28])
            j += 1
        if yr_list[i][:11] == 'INMET_CO_DF':
            cities_df[f'{yr}_{j}'] = (yr_list[i][17:-28])
            j += 1
        if yr_list[i][:11] == 'INMET_CO_GO':
            cities_go[f'{yr}_{j}'] = (yr_list[i][17:-28])
            j += 1
        if yr_list[i][:11] == 'INMET_NE_BA':
            cities_ba[f'{yr}_{j}'] = (yr_list[i][17:-28])
            j += 1
        i += 1

user_yr = input('Digite o ano ')
user_city = input('Digite a cidade ').upper()

user_yr_list = os.listdir(f'cities_temperatures/assets/{user_yr}/')
for file in user_yr_list:
    if re.search(f'{user_city}', file) != None:
        city_data = pd.read_csv(f'cities_temperatures/assets/{user_yr}/{file}', skiprows=8,
                                encoding='latin-1', on_bad_lines='skip', sep=';', usecols=[0, 7, 15, 18])
        city_data.rename(
            columns={city_data.iloc[:, 0].name: 'Data'}, inplace=True)
        city_data['Data'] = pd.to_datetime(city_data['Data'])
        city_data['TEMPERATURA DO AR - BULBO SECO, HORARIA (°C)'] = city_data['TEMPERATURA DO AR - BULBO SECO, HORARIA (°C)'].str.replace(
            ',', '.').str.replace('-9999', 'NaN').astype(float)
        city_data['UMIDADE RELATIVA DO AR, HORARIA (%)'] = city_data['UMIDADE RELATIVA DO AR, HORARIA (%)'].replace(
            ',', '.').replace(-9999, 'NaN').astype(float)
        city_data['VENTO, VELOCIDADE HORARIA (m/s)'] = city_data['VENTO, VELOCIDADE HORARIA (m/s)'].str.replace(
            ',', '.').str.replace('-9999', 'NaN').astype(float)

city_table = city_data.groupby(pd.Grouper( # type: ignore
    key='Data', axis=0, freq='M')).mean()
city_table.reset_index(inplace=True)
i = 0
for month in ['Jan', 'Fev', 'Mar', 'Abr', 'Mai', 'Jun', 'Jul', 'Ago', 'Set', 'Out', 'Nov', 'Dez']:
    city_table['Data'][i] = f'{month}/{user_yr[2:]}'
    i += 1

city_table.dropna(inplace=True)
fig = go.Figure(
    data=[go.Scatter(x=city_table['Data'],
                     y=city_table['TEMPERATURA DO AR - BULBO SECO, HORARIA (°C)'])],
    skip_invalid=True,
    empty=False,
    layout=go.Layout(title=go.layout.Title(
        text=f'Temperatura média/mês no ano de {user_yr} em {user_city.title()}'))
)
fig.update_layout(xaxis_title_text=f'Meses do ano',
                  yaxis_title_text='Temperatura média (ºC)')

if __name__ == '__main__':
    fig.write_html('cities_temperatures/city_temperature.html')
