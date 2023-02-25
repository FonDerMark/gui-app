import eel

eel.init('web')


@eel.expose
def test(text):
    return f"{text} = response"


eel.start('main.html', size=(400, 400))
