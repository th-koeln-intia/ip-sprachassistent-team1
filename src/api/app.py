from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello():
    return 'Hello World!'

from api import alarm
from api import light