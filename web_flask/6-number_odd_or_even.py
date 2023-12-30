#!/usr/bin/python3
"""
Starts a Flask web application
"""
from flask import Flask, render_template
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


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    """
    HTML template.
    """
    return render_template('5-number.html', num=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def number_odd_or_even(n):
    """
    Check if number is even or odd.
    """
    if n % 2 == 0:
        return render_template('6-number_odd_or_even.html', num=f'{n} is even')
    return render_template('6-number_odd_or_even.html', num=f'{n} is odd')


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
