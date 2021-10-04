"""
Flask App entry
"""

from flask import Flask
from middleware.test import test

app = Flask(__name__)


@app.route("/")
def index():
  test()
  return "<p>Hello, World!</p>"
