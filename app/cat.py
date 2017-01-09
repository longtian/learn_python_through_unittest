import base64
import webbrowser
from os.path import join, dirname


def encode_picture(target):
    with open(target, 'rb') as file:
        image_date = file.read()
        base64_data = base64.b64encode(image_date)
        webbrowser.open('data:image/jpg;base64,' + str(base64_data, 'ascii'))


encode_picture(join(dirname(__file__), '../cat_rocket.jpg'))
