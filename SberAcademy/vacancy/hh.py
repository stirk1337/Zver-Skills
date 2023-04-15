import requests
import json
from datetime import date
import re


def clean(text):
    example = re.compile(r'<[^>]+>')
    s = example.sub('', text).replace(' ', ' ').replace('\xa0', ' ').strip()
    return re.sub(" +", " ", s)


def get_hh_ru():
    today = date.today()
    rows = []
    for page in range(20):
        req = requests.get(
            f'https://api.hh.ru/vacancies?specialization=1&employer_id=3529&per_page=100&page={page}')
        data = req.content.decode()
        req.close()
        js = json.loads(data)
        for item in js['items']:
            if 'python' not in item['name'].lower() and 'питон' not in item['name'].lower():
                continue
            row = {}
            row['name'] = item['name']
            req = requests.get(
                f'https://api.hh.ru/vacancies/{item["id"]}')
            data = req.content.decode()
            req.close()
            js = json.loads(data)
            s = js['key_skills']
            row['description'] = clean(js['description'][:150])
            skills = []
            for skill in s:
                skills.append(skill['name'])
            skills = str(skills).replace('[', '').replace(']', '').replace("'", '')
            row['skills'] = skills
            row['employer'] = item['employer']['name']
            if item['salary'] is None:
                row['salary_from'] = 'None'
                row['salary_to'] = 'None'
                row['salary_currency'] = 'None'
            else:
                row['salary_from'] = item['salary']['from']
                row['salary_to'] = item['salary']['to']
                row['salary_currency'] = item['salary']['currency']
            row['area'] = item['area']['name']
            publ = item['published_at'].split('T')[1].split('+')
            row['published_at'] = publ[0]
            rows.append(row)
            if len(rows) == 10:
                return rows

    return rows


if __name__ == '__main__':
    print(get_hh_ru())
