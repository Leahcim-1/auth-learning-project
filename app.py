"""
Flask App entry
"""

from flask import Flask

app = Flask(__name__)


@app.route("/")
def index():
  return "<p>Hello, World!</p>"

@app.route ("/login")
def login(): 
  pass
