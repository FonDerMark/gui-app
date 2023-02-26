import eel


eel.init('web')


@eel.expose
def test():
    return 'Some text'


eel.start('main.html', size=(400, 400))