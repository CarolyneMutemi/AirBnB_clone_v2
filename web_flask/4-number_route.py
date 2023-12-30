#!/usr/bin/python3
"""
Starts a Flask web application
"""
from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def index():
    """
    Index page.
    """
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """
    HBNB page.
    """
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def get_text(text):
    """
    Get text from URL.
    """
    return f"C {text}".replace('_', " ")


@app.route('/python', defaults={'text': 'is_cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_text(text):
    """
    Print python text.
    """
    return f"Python {text}".replace('_', " ")


@app.route('/number/<int:n>', strict_slashes=False)
def get_number(n):
    """
    Get integer.
    """
    return f"{n} is a number"


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
