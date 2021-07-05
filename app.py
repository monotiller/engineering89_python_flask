# Creating a file called app.py
# Let's see how can we use Python Flask to interact with our browser
# Install flask: pip install flask

from flask import Flask

# We have to create an object this class
app = Flask(__name__) # Creating an app instance

# Let's create a function to link to our home/default page
# Let's connect this function to our browser
@app.route("/") # Decorating our function with @app.route to set route in our browser
def index():
    return "Welcome to Engineering 89 DevOps team"

# flask run

# Let's create a welcome page
@app.route("/welcome/") # / at the end is best practice to have as it would load the page in both cases
def welcome():
    return "<h1>Welcome</h1>"

# Create a decorator to route traffic to login page
# Display 2 messages of your choice in form of h1 and h2
@app.route("/login/")
def login():
    return "<h1>Login</h1><h2>Enter your credentials</h2>"