"""
Flask website for the LoiLibre project
"""

import flask
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    """
    Index page"""
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
