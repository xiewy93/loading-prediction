#http://flask.pocoo.org/
#http://docs.jinkan.org/docs/flask/quickstart.html#quickstart
#http://www.pythondoc.com/flask-mega-tutorial/
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'

if __name__ == '__main__':
    app.run()
