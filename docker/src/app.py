from flask import Flask

# initialize the app
app = Flask(__name__)

# define routes
@app.route('/')
def home():
    return """<h1 style='text-align:center; line-height:1.5; padding-top:150px'>
    Welcome to SCA Cloud School Application , <br> this is my first assessment
    </h1>"""