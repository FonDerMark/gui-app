import eel
from parse import news_finder


eel.init('web')


@eel.expose
def test() -> dict:
    return news_finder()


eel.start('main.html', size=(400, 400))
