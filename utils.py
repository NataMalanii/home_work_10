import requests

from config import path


def load_json():
    '''Получает список кандидатов с внешнего ресурса'''

    json_candidates = list(requests.get(path).json())
    return json_candidates


def get_candidates() -> str:
    '''Выводит информацию о кандидатах'''

    result = '<pre>'
    for candidate in load_json():
        result += f"""
        Имя кандидата: {candidate['name']}
        Позиция кандидата: {candidate['position']}
        Навыки кандидата: {candidate['skills'].lower()}
        """
    result += '</pre>'
    return result


def get_candidate_id(id: int) -> str:
    '''Выводит информацию о кандидате по его id'''

    for candidate in load_json():

        if candidate['id'] == id:
            candidate = f"""
                <pre>    
                <img src="{candidate["picture"]}">    
                Имя кандидата: {candidate['name']}
                Позиция кандидата: {candidate['position']}
                Навыки кандидата: {candidate['skills'].lower()}
                </pre>
                """
            return candidate

    return f"Такого кандидата нет"


def get_candidate_skills(skill: str) -> list:
    '''Выводит информацию о кандидате по его навыкам'''

    result = []
    for candidate in load_json():

        if skill.lower() in candidate['skills'].lower().split(', '):
            result.append(candidate)

    return result

