import json


def load_candidates():
    """Загружает данные из файла и передаёт переменной candidates_list"""
    with open("candidates.json", "r", encoding="utf-8") as file:
        candidates_list = json.load(file)
    return candidates_list


def get_candidate(candidate_id):
    """Возвращает кандидата по его id"""
    candidates = load_candidates()
    return [candidate for candidate in candidates if candidate["id"] == candidate_id]


def get_candidates_by_name(name):
    """Возвращает кандидата по части имени"""
    candidates = load_candidates()
    result = [candidate for candidate in candidates if name.lower() in candidate["name"].lower()]
    if not result:
        return "Кандидата с таким именем нет"
    else:
        return result


def get_candidates_by_skill(skill):
    """Возвращает кандидата по навыку"""
    candidates = load_candidates()
    return [candidate for candidate in candidates if skill.lower() in candidate["skills"].lower().split(", ")]
