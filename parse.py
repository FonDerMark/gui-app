import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent

url = 'https://www.msu.ru/science/'


def soup_creator():
    ua = UserAgent()
    headers = {
        'User-Agent': ua.random,
    }
    response = requests.get(url, headers=headers).text
    return BeautifulSoup(response, 'html.parser')


def news_finder():
    result = {}
    soup = soup_creator()
    news = soup.find('div', class_='news-list').findAll('div', class_='news-list-item')
    for n in news:
        id = n.get('id')
        date = n.find('div', class_='news-list-item-date').text
        main_theme = n.find('li', class_='news-list-tag_3').find('a').text
        image = 'https://www.msu.ru' + n.find('img').get('src')
        text = n.find('div', class_='news-list-item-text').text
        link = 'https://www.msu.ru' + n.find('div', class_='news-list-item-head').find('a').get('href')
        result[id] = {
            'date': date,
            'main_theme': main_theme,
            'image': image,
            'text': text,
            'link': link,
        }
    return result


if __name__ == '__main__':
    print(news_finder())
