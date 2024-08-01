from flask import (
    Flask,
    flash,
    get_flashed_messages,
    redirect,
    render_template,
    request,
    session,
    url_for,
)
from hashlib import sha256

app = Flask(__name__)
app.secret_key = ' '


users = [
    {'name': 'tota', 'password': sha256(b'password123').hexdigest()},
    {'name': 'alice', 'password': sha256(b'donthackme').hexdigest()},
    {'name': 'bob', 'password': sha256(b'qwerty').hexdigest()},
]


def get_user(form_data, repo):
    name = form_data['name']
    password = sha256(form_data['password'].encode()).hexdigest()
    for user in repo:
        if user['name'] == name and user['password'] == password:
            return user


@app.route('/')
def index():
    messages = get_flashed_messages(with_categories=True)
    current_user = session.get('user')
    return render_template(
        'index.html',
        messages=messages,
        current_user=current_user,
        )


# BEGIN (write your solution here)
@app.post('/session/new')
def new_session():
    data = request.form.to_dict()
    user = get_user(data, users)
    if not user:
        flash('Wrong password or name', 'warning')
        return redirect(url_for('index'))
    session['user'] = user
    return redirect(url_for('index'))


@app.route('/session/delete', methods=['POST', 'DELETE'])
def delete_session():
    session.clear()
    return redirect(url_for('index'))
# END
