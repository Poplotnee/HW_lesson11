import json


def load_candidates_from_json():
    with open('candidates.json', 'r', encoding='utf-8') as file:
        candidates = json.load(file)
        return candidates


def get_candidate(candidate_id):
    candidates = load_candidates_from_json()
    for candidate in candidates:
        if candidate['pk'] == candidate_id:
            return candidate


def get_candidates_by_name(candidate_name):
    find_list_name = []
    candidates = load_candidates_from_json()
    for candidate in candidates:
        if candidate_name.lower() in candidate['name'].lower():
            find_list_name.append(candidate)
    return find_list_name


def get_candidates_by_skill(skill_name):
    find_list_skill = []
    candidates = load_candidates_from_json()
    for candidate in candidates:
        if skill_name.lower() in candidate['skills'].lower():
            find_list_skill.append(candidate)
    return find_list_skill
