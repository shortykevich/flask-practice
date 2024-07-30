from flask import Flask, render_template, url_for

from lessons_practice.data import generate_users

users = generate_users(100)

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


# BEGIN (write your solution here)
@app.route('/users')
def get_users():
    return render_template(
        'users/index.html',
        users=users,
    )


@app.route('/users/<int:id>')
def show_user(id):
    filtered_users = filter(lambda user: user['id'] == id, users)
    found_user = next(filtered_users, None)

    if found_user is None:
        return 'Page not found', 404
    return render_template(
        'users/show.html',
        user=dict(found_user),
    )
# END
