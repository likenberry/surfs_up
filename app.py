# Import dependencies
from flask import Flask

# Creating new flask instance
app = Flask(__name__)

# Creating flask routes
@app.route('/')

# Testing a route
@app.route('/')
def hello_world():
    return 'Hello World'

# Running the flask app
# run in the terminal as one command:
# export FLASK_APP=app.py flask run

# Trying something
if __name__ == "__main__":
    app.run()