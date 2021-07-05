# Model View Controller (MVC) with Python Flask
## Python Flask
- Flask is python micro-framework

Creating a file called app.py

Let's see how can we use Python Flask to interact with our browser

Install flask: `pip install flask`
```python
from flask import Flask
```
We have to create an object this class
```python
app = Flask(__name__) # Creating an app instance
```
Let's create a function to link to our home/default page

Let's connect this function to our browser
```python
@app.route("/") # Decorating our function with @app.route to set route in our browser
def index():
    return "Welcome to Engineering 89 DevOps team"
```
Then type `flask run` into your terminal. It should display:
> Welcome to Engineering 89 DevOps team

On screen

Let's create a welcome page
```python
@app.route("/welcome/") # / at the end is best practice to have as it would load the page in both cases
def welcome():
    return "<h1>Welcome</h1>"
```
Which should display:
> <h1>Welcome</h1>

On screen
```python
@app.route("/login/")
def login():
    return "<h1>Login</h1><h2>Enter your credentials</h2>"
```
Which should display:
> <h1>Login</h1>
> <h2>Enter your credentials</h2>

On screen