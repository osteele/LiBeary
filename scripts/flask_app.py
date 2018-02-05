"""
A basic flask app for deployment purposes
"""

from flask import render_template
from flask import Flask
app = Flask(__name__)


@app.route('/')
def hello_world():
    return "Hello World"


if __name__ == '__main__':
    app.run()