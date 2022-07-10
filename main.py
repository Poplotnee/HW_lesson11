from flask import Flask

from utils import get_all, get_by_pk, get_by_skill

app = Flask(__name__)


@app.route("/")
def page_index():
    return get_all()


@app.route('/users/<int:uid>')
def page_users(uid):
    return get_by_pk(uid)


@app.route('/skill/<skill>')
def page_skills(skill):
    return get_by_skill(skill)


if __name__ == "__main__":
    app.run()
