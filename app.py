#Import flask
from flask import Flask

# Create new flask app instance
app = Flask(__name__)

# Create route - root
@app.route('/')
def hello_world():
    return 'Hello world'
