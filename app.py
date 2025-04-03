"""Simple Flask application following best practices."""

from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    """Handles the home route and returns a simple greeting message."""
    return "USN: 1RVU23CSE019"

if __name__ == '__main__':
    app.run(debug=True)
