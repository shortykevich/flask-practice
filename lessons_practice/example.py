from flask import Flask, jsonify, request
from lessons_practice.data import generate_companies


app = Flask(__name__)
companies = generate_companies(100)


@app.route('/')
def index():
    return "<a href='/companies'>Companies</a>"


@app.route('/companies')
def get_companies():
    page = request.args.get('page', default=1, type=int)
    per = request.args.get('per', default=5, type=int)
    target_page = ((page - 1) * per)
    return jsonify(companies[target_page:target_page + per])

