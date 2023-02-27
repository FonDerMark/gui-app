import json
import eel
from parse import news_finder


eel.init('web')


@eel.expose
def test() -> json:
    return json.dumps(news_finder(), ensure_ascii=False)


eel.start('main.html', size=(600, 600))
