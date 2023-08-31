from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello World"

@app.route('/novo')
def novo():
     return "Olá Mundo!"


app.run()
