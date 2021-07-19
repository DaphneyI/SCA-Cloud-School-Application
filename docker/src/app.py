from flask import Flask

# initialize the app
app = Flask(__name__)

# define routes
@app.route('/')
def home():
    return """<h1 style='text-align:center; text-transform:capitalize'>Welcome to SCA Cloud School Application</h1>"""