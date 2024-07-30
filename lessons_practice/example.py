from flask import Flask, jsonify

from lessons_practice.data import generate_companies

companies = generate_companies(100)

app = Flask(__name__)


@app.route('/')
def index():
    return 'open something like (you can change id): /companies/5'


@app.route('/companies/<int:id>')
def get_company(id):
    found_company = [company for company in companies if company['id'] == id]
    if found_company:
        return jsonify(found_company[0])
    return 'Page not found', 404
