from flask import Flask, render_template

from utils import load_candidates_from_json, get_candidate, get_candidates_by_name, get_candidates_by_skill

app = Flask(__name__)


@app.route("/")
def page_index():
    candidates = load_candidates_from_json()
    return render_template('card.html', candidates=candidates)


@app.route("/candidate/<int:candidate_id>")
def page_candidate(candidate_id):
    candidate = get_candidate(candidate_id)
    return render_template('single.html', candidate=candidate)


@app.route("/search/<candidate_name>")
def page_search(candidate_name):
    find_list_name = get_candidates_by_name(candidate_name)
    return render_template('search.html', candidates=find_list_name)


@app.route("/skill/<skill_name>")
def page_skill_search(skill_name):
    find_list_skill = get_candidates_by_skill(skill_name)
    return render_template('skill.html', candidates=find_list_skill, skill_name=skill_name)


if __name__ == "__main__":
    app.run()
