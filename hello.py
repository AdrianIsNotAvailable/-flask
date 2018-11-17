from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return '<h1>Hello, world ! <\h1>'

@app.route('/route')
def owca():
    return '<h1> Owce są fajne <\h1>'