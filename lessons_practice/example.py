from flask import Flask, render_template, request
from lessons_practice.repository import PostsRepository

app = Flask(__name__)

repo = PostsRepository(50)


@app.route('/')
def index():
    return render_template('index.html')


# BEGIN (write your solution here)
@app.route('/posts/<slug>')
def show_post(slug):
    post = repo.find(slug)

    if not post:
        return 'Page not found', 404

    return render_template(
        'posts/show.html',
        post=post
    )


@app.route('/posts')
def show_posts():
    posts = repo.content()
    page = request.args.get('page', default=1, type=int)
    per_page = 5

    target_page = ((page - 1) * per_page)
    next_page = page if page == len(posts) // per_page else page + 1
    prev_page = page if page == 1 else page - 1
    return render_template(
        'posts/index.html',
        posts=posts[target_page:target_page + per_page],
        next_page=next_page,
        prev_page=prev_page
    )
# END
