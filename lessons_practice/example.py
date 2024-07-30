from flask import Flask, render_template, request
from lessons_practice.data import generate_users


users = generate_users(100)

app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template(
        'index.html',
    )


@app.route('/users')
def get_users():
    term = request.args.get('term', '').lower()

    filtered_users = filter(
            lambda user: user['first_name'].lower().startswith(term),
            users
    )

    return render_template(
        'users/index.html',
        term=term,
        users=filtered_users,
    )
