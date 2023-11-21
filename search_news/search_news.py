from GoogleNews import GoogleNews
import pandas as pd

googlenews = GoogleNews(encode='utf-8', lang='pt', period='90d')

googlenews.get_news('Data science')
result = googlenews.results(sort=True)
df = pd.DataFrame(result)

def search_news(user_lang, user_period, user_search, user_count):
    googlenews = GoogleNews(encode='utf-8', lang=user_lang, period=user_period+'d')
    googlenews.get_news(user_search)
    result = googlenews.results(sort=True)
    for _ in range(0, user_count):
        print(result)


if __name__ == '__main__':
    search_news('pt', '80', 'carro', 10)