from flask import Flask

app = Flask(__name__, static_url_path='',
            root_path='../IMAGE-CLASSIFIER-EXAMPLE/', static_folder='frontend')
app.secret_key = "secret key"
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024
