import eel
import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
import lxml

# eel.init('web')

url = 'https://hubblesite.org/resource-gallery/images'


@eel.expose
def test():
    ua = UserAgent()
    headers = {
        'User-Agent': ua.random,
    }
    response = requests.get(url, headers=headers).content
    soup = BeautifulSoup(response, 'html.parser')
    result = soup.findAll('picture')
    for i in result:
        print(i)
    return soup.prettify()


# eel.start('main.html', size=(400, 400))

if __name__ == '__main__':
    test()
