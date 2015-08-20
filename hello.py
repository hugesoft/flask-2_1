from flask import Flask
from flask import request
from flask import redirect
from flask.ext.script import Manager

app = Flask(__name__)
manager = Manager(app)

@app.route('/')
def index():
    return redirect('http://www.hz66.com')

if(__name__ == '__main__'):
    manager.run()
