import requests as rq

with open('weather_api/.secret.txt') as file:
    api_key = file.read()

city = 'rio de janeiro'

weather = rq.get(f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&lang=pt_br&units=metric')
weather_dic = weather.json()
print(weather_dic, '\n')

weather_temp = round(weather_dic['main']['temp'])
weather_img = f"https://openweathermap.org/img/wn/{weather_dic['weather'][0]['icon']}.png"
weather_desc = weather_dic['weather'][0]['description'].title()
weather_hum = weather_dic['main']['humidity']
city_name = weather_dic['name'].title()

if __name__ == '__main__':
    print(f'Temperatura: {weather_temp} \nDescrição: {weather_desc} \nLink imagem: {weather_img} \nUmidade relativa do ar: {weather_hum} \nCidade: {city_name}')