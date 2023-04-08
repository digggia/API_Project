import json
import requests


def api_request(heroes):
    url = 'https://akabab.github.io/superhero-api/api/all.json'
    hero_dict = json.loads(requests.get(url).content)
    max_intelligence = 0

    for hero_item in hero_dict:
        if hero_item['name'] in heroes:
            if hero_item['powerstats'].get('intelligence') > max_intelligence:
                max_intelligence = hero_item['powerstats'].get('intelligence')
                max_hero_name = hero_item['name']

    res = f'{max_hero_name} самый умный, его показатель: {max_intelligence}\n'
    return res

heroes_list = ['Hulk', 'Captain America', 'Thanos']
print(api_request(heroes_list))