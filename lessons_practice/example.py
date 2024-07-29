from flask import Flask
from flask import request

# Это callable WSGI-приложение
app = Flask(__name__)


@app.route('/')
def index():
    return 'Hello, World!'

# 1st example of methods indication:
# @app.get('/users')
# def users_get():
#     return 'GET /users'
#
#
# @app.post('/users')
# def users_post():
#     return 'POST /users'


# 2nd example of methods indication:
@app.route('/users', methods=['GET', 'POST'])
def users():
    return f'Hello from {request.method} /users'
