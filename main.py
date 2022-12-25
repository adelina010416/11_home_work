from flask import Flask, render_template
from utils import load_candidates, get_candidate, get_candidates_by_name, get_candidates_by_skill


app = Flask(__name__)


@app.route("/")
@app.route("/home")
def page_index():
    """Выводит список всех кандидатов"""
    candidates = load_candidates()
    page = render_template("list.html", candidates=candidates)
    return page


@app.route("/candidate/<int:cand_id>")
def profile(cand_id):
    """Возвращает страничку кандидата с заданным id"""
    candidate = get_candidate(cand_id)
    candidate = candidate
    page = render_template("card.html", candidate=candidate[0])
    return page


@app.route("/request/<name>")
def cand_name(name):
    """Возвращает список кандидатов, в имени которых содержатся введённые символы"""
    candidates = get_candidates_by_name(name)
    if candidates == "Кандидата с таким именем нет":
        return f'<a href="../home">На главную</a><br>{candidates}'
    else:
        amount = len(candidates)
        page = render_template("search.html", candidates=candidates, amount=amount)
        return page


@app.route("/skill/<skill_name>")
def cand_skill(skill_name):
    """Возвращает список кандидатов, у которых есть заданный навык"""
    candidates = get_candidates_by_skill(skill_name)
    amount = len(candidates)
    page = render_template("skill.html", candidates=candidates, amount=amount, skill=skill_name)
    return page


if __name__ == "__main__":
    app.run(debug=True)
